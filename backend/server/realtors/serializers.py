from rest_framework import serializers
from .models import Realtor

class RealtorSerializer(serializers.ModelSerializer):
    """serialize the Realtor model"""
    class Meta:
        model = Realtor
        fields = '__all__'