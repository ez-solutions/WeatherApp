from __future__ import unicode_literals
from passlib.hash import sha256_crypt
import re

from django import forms
from django.core.validators import RegexValidator


from . import models


TEL_REGEX = "^((?:\+27|27)|0)[\s-]?(\d{2})[\s-]?(\d{3})[\s-]?(\d{4})[\s]*$"


class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(
            min_length=8, widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


    def clean_password(self):
        password = self.cleaned_data['password']
        return sha256_crypt.encrypt(password)

    def clean_password_repeat(self):
        password_repeat = self.cleaned_data['password_repeat']
        try:
            password = self.cleaned_data['password']
        except KeyError:
            raise forms.ValidationError('Password is required')

        if not sha256_crypt.verify(password_repeat, password):
            raise forms.ValidationError('Passwords must match')

        return password


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
            min_length=8, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not password or not email:
            raise forms.ValidationError('All fields are required')

        error_msg = 'Problem with login, please check details and try again'
        try:
            user = models.User.objects.get(email=email)
        except:
            raise forms.ValidationError(error_msg)

        if not user.is_authentic(password):
            raise forms.ValidationError(error_msg)
