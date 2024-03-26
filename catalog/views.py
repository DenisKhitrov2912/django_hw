from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

from pytils.translit import slugify

from .forms import ProductForm, VersionForm, PermProductForm
from .models import Product, Contacts, BlogWriting, Version, Category

from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView

from .services import get_categories


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts_fill = Contacts.objects.all()
        context['contacts'] = contacts_fill
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
        return render(request, self.template_name)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    ordering = ['-created_at']
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_products = Product.objects.order_by('-created_at')[:2]
        context['latest_products'] = latest_products
        print(context['latest_products'])
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = 'users:login'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'
    permission_required = ('catalog.set_published', 'catalog.change_description', 'catalog.change_category',)

    def get_form_class(self):
        if self.request.user.has_perm('catalog.set_published') and self.request.user.has_perm(
                'catalog.change_description') and self.request.user.has_perm(
            'catalog.change_category') and not self.request.user.is_superuser:
            return PermProductForm
        return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        else:
            return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            num_active_versions = [form for form in formset if form.cleaned_data.get('is_current')]
            if len(num_active_versions) > 1:
                form.add_error(None, 'Выберите только одну версию прордукта!')
                return self.form_invalid(form)
            formset.instance = self.object
            formset.save()
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductsListView(ProductListView):
    template_name = 'catalog/products_list.html'
    paginate_by = 1
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.get_queryset()
        paginator = Paginator(object_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context['object_list'] = objects
        return context


class BlogWritingCreateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogWriting
    fields = (
        'title', 'context', 'image', 'is_published',)
    success_url = reverse_lazy('catalog:blogwrite_readall')
    permission_required = 'catalog.add_blogwriting'

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_content_manager


class BlogWritingDetailView(DetailView):
    model = BlogWriting

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        if self.object.count_of_views == 3:
            send_mail(
                'Поздравляем с достижением 3 просмотров!',
                'Ваша статья достигла 3 просмотров. Поздравляем!',
                settings.EMAIL_HOST_USER,
                ['hitrov.95@yandex.ru'],
                fail_silently=False,
            )
        return self.object


class BlogWritingListView(ListView):
    model = BlogWriting

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_published=True)
    #     return queryset


class BlogWritingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogWriting
    fields = (
        'title', 'context', 'image', 'is_published',)
    permission_required = 'catalog.change_blogwriting'

    def get_success_url(self):
        return reverse_lazy('catalog:blogwrite_read', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_content_manager


class BlogWritingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogWriting
    success_url = reverse_lazy('catalog:blogwrite_readall')
    permission_required = 'catalog.delete_blogwriting'

    def test_func(self):
        return self.request.user.is_content_manager


def category_list_view(request):
    return render(request, 'catalog/category_list.html', get_categories())
