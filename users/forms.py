from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        """Переопределение формы"""
        super().__init__(*args, **kwargs)
        #  прячем поле с паролем в профиле
        self.fields['password'].widget = forms.HiddenInput()

