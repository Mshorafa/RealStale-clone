import datetime
from django.db import models
from django.utils import timezone
from core import models as core_model

# Create your models here.
class Realtor (core_model.TimeStampedModel):
    """This Class for modelsing thr Person of Realtor"""
    name = models.CharField(max_length=50)
    avater = models.ImageField(upload_to='avater')
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return f'{self.name}'
