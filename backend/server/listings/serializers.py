from rest_framework import serializers

from .models import Listing


class ListingsSerializer(serializers.ModelSerializer):
    """serializer for all listings data"""
    class Meta:
        model = Listing
        fields = ['title', 'address', 'location', 'county', 'sale_type', 'house_type', 'main_photo', 'list_date', 'open_house']
        