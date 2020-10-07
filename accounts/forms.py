from django import forms
from django.contrib.auth.models import User
from django.contrib import messages

# Create your forms here.


class registerForms(forms.Form):
    first_name = forms.CharField(max_length=50,label='First Name')
    last_name = forms.CharField(max_length=50,label='Last Name')
    username = forms.CharField(max_length=50,label='Username')
    email = forms.EmailField(max_length=50,label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('The Email is All ready exits' ,code='Exits User')
        except User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        print("**",password,password1)

        if password != password1:
            raise forms.ValidationError('The password doesnt match')
        else:
            return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('The Username is all ready exits' , code='Exits Username')
        except User.DoesNotExist:
            return username

    def save(self):
        User.save(commit=False)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        User.username=username
        User.set_password(password)
        User.save()



