from django.shortcuts import render
from .forms import ProductForm
from .models import Product, Contacts


def contacts(request):
    contacts_fill = Contacts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contacts.html', {'contacts': contacts_fill})


def home(request):
    latest_products = Product.objects.order_by('-created_at')[
                      :2]  # выборка последних двух товаров (у меня их мало просто)
    for product in latest_products:
        print(product)
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(id=pk)
    }
    return render(request, 'catalog/products.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    return render(request, 'catalog/add_product.html', {'form': form})
