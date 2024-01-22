from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    # serializer for all listings in the database
    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'state', 'price', 'sale_type',
                  'property_type', 'bedrooms', 'bathrooms', 'size', 'photo_main', 'slug']


class ListingDetailSerializer(serializers.ModelSerializer):
    # view a single serializer in details
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'
