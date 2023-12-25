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