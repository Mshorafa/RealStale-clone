from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from . import forms

from Lsitings import models as listing_modle


# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'Welcome {username} ;) ')
            return redirect(reverse('core:index'))
        else:
            messages.error(request,'You dont have permeation to login ')
            return redirect(reverse('accounts:login'))
    return render(request,'accounts/login.html', {})


def register(request):
    if request.method == 'POST':
        form = forms.registerForms(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            last_name = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,'You can login now')
            return redirect(reverse('accounts:login'))
        else:
            messages.error(request, form.errors)

    else:
        form = forms.registerForms()
    return render(request,'accounts/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request,'Your are logout')
    return redirect(reverse('core:index'))


def dashboard(request):
    user = request.user.id
    if user is not None:
        listing_user = listing_modle.Listings.objects.filter(realtors__id=user).order_by('created')
        return render(request, 'accounts/dashboard.html', {'listing_user': listing_user})

    else:
        messages.error(request,'You dont have permeation to go there')
        return render(request, 'accounts/dashboard.html')


