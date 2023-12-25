from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Realtor
from .serializers import RealtorSerializer


class RealtorListView(ListAPIView):
    """displays all registered realtors"""
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None

class RealtorView(RetrieveAPIView):
    """display a specif realtor"""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    """display the top sellers"""
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.filter(is_top_seller=True)
    serializer_class =RealtorSerializer
    pagination_class = None
    