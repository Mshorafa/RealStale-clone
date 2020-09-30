from django.shortcuts import render
from django.db.models import Q

from Lsitings import models as Lsitings_mode
from Realtors import models as Roaltors_model


# Create your views here.


def index(request):
    last_Listings = Lsitings_mode.Listings.objects.filter(is_published=True).order_by('created')[:3]
    return render(request,'Pages/index.html', {'listings':last_Listings})


def about(request):
    top_realtors = Roaltors_model.Realtor.objects.all().order_by('-created')[:3]
    try:
        top_re = Roaltors_model.Realtor.objects.filter(is_mvp=True).order_by('-updated')[:1]
        return render(request, 'Pages/about.html', {'realtors': top_realtors, 'tops': top_re})
    except Roaltors_model.Realtor.DoesNotExist:
        return 0


def search(request):
    return  render(request,'Pages/search.html')
