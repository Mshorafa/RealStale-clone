from django.shortcuts import render, Http404
from django.core.paginator import Paginator
from . import models as lsitings_model
from Realtors import models as Roaltors_model



# Create your views here.


def listings(request):
    _listings = lsitings_model.Listings.objects.filter(is_published=True).order_by('-created')
    paginator = Paginator(_listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listings/listings.html', {'listings': page_obj})


def listing(request,pk):
    try:
        pk_listing = lsitings_model.Listings.objects.get(pk=pk)
        top_re, = Roaltors_model.Realtor.objects.filter(is_mvp=True).order_by('-updated')[:1]
        return render(request, 'listings/listing.html', {'listing': pk_listing,'top_re': top_re})
    except lsitings_model.Listings.DoesNotExist:
        raise Http404()


def serach(request):
    return render(request, 'listings/serach.html')
