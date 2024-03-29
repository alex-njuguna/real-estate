from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor
from autoslug import AutoSlugField


class Listing(models.Model):
    # table that contains a listing data
    class SaleType(models.TextChoices):
        # choices for the type of sale
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class PropertyType(models.TextChoices):
        # home option
        HOUSE = 'House'
        APARTMENT = 'Apartment'
        TOWNHOUSE = 'Townhouse'
        LAND = 'Land'
        OFFICE = 'Office'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title',
                         editable=True, always_update=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    property_type = models.CharField(
        max_length=50, choices=PropertyType.choices, default=PropertyType.HOUSE)
    size = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_19 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_20 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
