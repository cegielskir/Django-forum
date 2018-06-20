from django.contrib.auth.models import User
from django import forms
from .models import Answer


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class AnswerAddForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Answer
        fields =['text']


class TopicAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Answer
        fields = ['title', 'text']

