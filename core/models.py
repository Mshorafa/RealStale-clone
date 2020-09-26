from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stamped Model  """
    created = models.DateTimeField(auto_now_add=True)  # Add Time and Date in the First Created
    updated = models.DateTimeField(auto_now=True)      # Add Time and Date every time the model saved

    class Meta:
        abstract = True