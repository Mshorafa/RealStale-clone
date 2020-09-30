from django.contrib import admin
from django.forms import CheckboxInput

from . import models
# Register your models here.


@admin.register(models.Realtor)
class CustomRealtorsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'avater',
        'phone',
        'email',
        'is_mvp',
        'hire_date',
    ]
    list_editable = ['is_mvp',]