from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify

from realtors.models import Realtor


class Listing(models.Model):
    """A table with details of a listing"""
    SALE_TYPE = (
        ('for sale', 'for sale'),
        ('for rent', 'for rent')
    )

    HOME_TYPE = (
        ('house', 'house'),
        ('apartment', 'apartment')
    )

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    description = models.TextField()
    sale_type = models.CharField(max_length=15, choices=SALE_TYPE, default='for sale')
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length=15, choices=HOME_TYPE, default='house')
    size = models.IntegerField()
    open_house = models.BooleanField(default=True)
    main_photo = models.ImageField(upload_to='listings/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_11 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_12 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_13 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_14 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_15 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_16 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_17 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_18 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_19 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    photo_20 = models.ImageField(upload_to='listings/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.location}({self.county})'

