from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from datetime import timezone, datetime, timedelta

from .models import Listing
from .serializers import ListingsSerializer, ListingSerializer


class ListingsView(ListAPIView):
    """display all listings"""
    permission_classes = (permissions.AllowAny,)
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingsSerializer
    lookup_field = 'slug'

class ListingDetailView(RetrieveAPIView):
    """diplay a single listing"""
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'