from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Photo)
class CustomPhotoAdmin(admin.ModelAdmin):
    pass


class photo_inline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Listings)
class CustomListingsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'address',
        'city',
        'state',
        'price',
        'bedroom',
        'bathroom',
        'garage',
        'sqft',
        'lot_size',
        'is_published',
        'realtors',
    ]
    list_display_links = ['title', 'address']
    list_filter = ['city', 'is_published']
    search_fields = ['title','city', 'state', 'state', 'price']
    list_editable = ['is_published',]


    inlines = (photo_inline,)



