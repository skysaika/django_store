from random import randint


from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User
from django.urls import reverse_lazy, reverse


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
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        """Метод отправки письма с регистрацией"""
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='ВЫ зарегистрировались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],

        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    """Контроллер для редактирования профиля пользователя"""
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')


    def get_object(self, queryset=None):
        """Получение объекта пользователя"""
        return self.request.user


def generate_new_password(request):
    """Контроллер для генерации нового пароля"""
    new_password = ''.join([str(randint(0, 9)) for _ in range(12)])

    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))


