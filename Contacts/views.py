from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


from . import models

# Create your views here.


def contact(request):
    pk = request.POST.get('listing_id')
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        realtor_email = request.POST.get('realtor_email')
        user_id = request.POST.get('user_id')

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contact = models.Contacts.objects.filter(listing_id=listing_id,user_id=user_id)
            if has_contact:
                messages.error(request,'You all ready make An Inquiry for this listing ')
                return redirect(reverse('lsitings:listing', kwargs={'pk': listing_id}))

        contact = models.Contacts.objects.create(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail('Property Listing Inequity',
                  f'There has been an Inquiry for {listing} sign int admin panel for more info {message} ',
                  settings.EMAIL_HOST_USER,
                  [realtor_email,'geo.shurafa@gmail.com'],
                  fail_silently=False
                  )

        messages.success(request,'Your  request has been submitted , realtors will get you soon')
        return redirect(reverse('lsitings:listing',kwargs={'pk':listing_id}))
    return redirect(reverse('lsitings:listing',kwargs={'pk':pk}))