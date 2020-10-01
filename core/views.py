from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from Lsitings import models as Lsitings_mode
from Realtors import models as Roaltors_model
from Lsitings import Choices


# Create your views here.


def index(request):
    last_Listings = Lsitings_mode.Listings.objects.filter(is_published=True).order_by('created')[:3]
    cites = Lsitings_mode.Listings.objects.values('city')
    state = Lsitings_mode.Listings.objects.values('state')
    context = {
        'listings': last_Listings,
        'bedroom_choices': Choices.bedroom_choices,
        'price_choices': Choices.price_choices,
        'state_choices': Choices.bedroom_choices,
        'cites': cites,
        'state': state,
    }

    return render(request, 'Pages/index.html', context)


def about(request):
    top_realtors = Roaltors_model.Realtor.objects.all().order_by('-created')[:3]
    try:
        top_re = Roaltors_model.Realtor.objects.filter(is_mvp=True).order_by('-updated')[:1]
        return render(request, 'Pages/about.html', {'realtors': top_realtors, 'tops': top_re})
    except Roaltors_model.Realtor.DoesNotExist:
        return 0


def search(request):
    cites = Lsitings_mode.Listings.objects.values('city')
    states = Lsitings_mode.Listings.objects.values('state')
    try:
       filter_list = {}
       if 'keywords' in request.GET:
           keyword = request.GET['keywords']
           if keyword != '':
               filter_list['description__icontains'] = keyword

       if 'city' in request.GET:
           city = request.GET['city']
           filter_list['city__iexact'] = city

       if 'state' in request.GET:
           state = request.GET['state']
           filter_list['state__iexact'] = state

       if 'bedroom' in request.GET:
           bedroom = request.GET['bedroom']
           filter_list['bedroom__lte'] = bedroom

       if 'price' in request.GET:
           price = request.GET['price']
           filter_list['price__lte'] = price

       _listings = Lsitings_mode.Listings.objects.filter(is_published=True, **filter_list ).order_by('-created')
       paginator = Paginator(_listings, 3)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)
       context = {
            'bedroom_choices': Choices.bedroom_choices,
            'price_choices': Choices.price_choices,
            'state_choices': Choices.bedroom_choices,
            'cites': cites,
            'states': states,
            'listings': page_obj,
       }
       return render(request, 'Pages/search.html', context)
    except Lsitings_mode.Listings.DoesNotExist:
        return None

