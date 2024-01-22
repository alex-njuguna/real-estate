from rest_framework import serializers

from .models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    # serializer for the realtor model
    class Meta:
        model = Realtor
        fields = '__all__'
