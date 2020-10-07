from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Contacts)
class CustomContacts(admin.ModelAdmin):
    list_display = ['listing',
                    'name',
                    'email',
                    'phone',
                    'contact',
                    ]

    search_fields = ['listing',
                     'name',
                     'email']

    list_display_links = [
        'listing',
        'name'
    ]

    list_per_page = 25
