import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail

from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView, TemplateView

from users.forms import UserRegisterForm, UserForm, UserPasswordResetForm
from users.models import User

from django.urls import reverse_lazy


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        email = form.get_user()
        user = User.objects.get(email=email)
        if not user.is_verificated:
            messages.error(self.request, 'Ваш email не верифицирован. Верифицируйте его с помощью ссылки в письме.')
            return redirect('users:login')
        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    template_name = 'users/register.html'


def email_verification(request, token):
    try:
        user = User.objects.get(verification_token=token)
        user.is_verificated = True
        user.save()
        return redirect('users:login')
    except User.DoesNotExist:
        raise Http404("User does not exist")


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(FormView):
    template_name = 'users/user_password_reset.html'
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('users:user_password_sent')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()

        if user is not None:
            characters = string.ascii_letters + string.digits
            new_password = ''.join(random.choice(characters) for i in range(12))

            user.password = make_password(new_password)
            user.save()

            subject = 'Восстановление пароля'
            message = f'Ваш новый пароль: {new_password}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

        return super().form_valid(form)


class UserPasswordSentView(TemplateView):
    template_name = 'users/user_password_sent.html'