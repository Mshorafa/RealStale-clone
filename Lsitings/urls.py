from django.urls import path
from . import views

app_name = 'lsitings'

urlpatterns =[
    path('', views.listings, name='listings'),
    path('listing/<int:pk>', views.listing, name='listing'),
    path('serach/', views.serach, name='serach'),
]