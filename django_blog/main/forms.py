from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_again = forms.CharField(label='Password again', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_again = cleaned_data.get('password_again')
        if User.objects.filter(username=username).count():
            raise ValidationError("User already exists")
        if password != password_again:
            self.add_error("password", "Passwords not match")


class LoginForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('nickname')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('Incorrect username or password')


class CommentForm(forms.Form):
    message = forms.CharField(label='')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['placeholder'] = 'Leave a comment...'


class NewArticleForm(forms.Form):
    title = forms.CharField(label='Article title')
    content = forms.CharField(label='New article')

