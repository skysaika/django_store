from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import User
from django.urls import reverse_lazy


# Create your views here.


class LoginView(BaseLoginView):
    """Вывод формы входа в систему"""
    template_name = 'users/login.html'


class LogoutView(BaseLoginView):
    """Вывод формы выхода из системы"""
    pass


class RegisterView(CreateView):
    """Вывод формы регистрации"""
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='ВЫ зарегистрировались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],

        )
        return super().form_valid(form)



