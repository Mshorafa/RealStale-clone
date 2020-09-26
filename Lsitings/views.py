from django.shortcuts import render
from django.core.paginator import Paginator
from . import models as lsitings_model


# Create your views here.


def listings(request):
    _listings = lsitings_model.Listings.objects.all()
    paginator = Paginator(_listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listings/listings.html', {'listings': page_obj})


def listing(request,pk):
    return render(request, 'listings/listing.html')


def serach(request):
    return render(request, 'listings/serach.html')
