from django.db import models
from core import models as core_model

# Create your models here.
class Photo(core_model.TimeStampedModel):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='photos')
    listing = models.ForeignKey('Listings', on_delete=models.CASCADE, related_name='Photo')
    main_photo = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return f'{self.name}'


class Listings(core_model.TimeStampedModel):
    """This model for listing fields """
    title = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    realtors = models.ForeignKey('Realtors.Realtor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}'

    def get_main_photo(self):
        try:
            main_photo_1 = self.Photo.get(main_photo=True)
            return main_photo_1.img.url
        except ValueError:
            None
