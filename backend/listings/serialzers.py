from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    # serializer for all listings in the database
    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'price', 'sale_type',
                  'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug']
