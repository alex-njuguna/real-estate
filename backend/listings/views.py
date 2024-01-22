from datetime import datetime, timezone, timedelta
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Listing
from .serialzers import ListingSerializer, ListingDetailSerializer


class ListingsView(ListAPIView):
    # display all listings with a link to a specific listing
    permission_classes = (permissions.AllowAny,)
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'


class ListingView(RetrieveAPIView):
    # display a single listing
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'
