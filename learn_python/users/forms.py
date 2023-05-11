from django import forms
import django.contrib.auth.forms
from django.contrib.auth.models import User


FORM_ATTRS = {'class': 'form-control'}


class RegisterUserForm(django.contrib.auth.forms.UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs=FORM_ATTRS),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=FORM_ATTRS),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs=FORM_ATTRS),
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs=FORM_ATTRS),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(django.contrib.auth.forms.AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs=FORM_ATTRS),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs=FORM_ATTRS),
    )


class UpdateUserForm(django.forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs=FORM_ATTRS),
        required=False,
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs=FORM_ATTRS),
        required=False,
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=FORM_ATTRS),
        required=True,
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
