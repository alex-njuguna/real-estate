from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Realtor
from .serializers import RealtorSerializer


class RealtorListView(ListAPIView):
    # display all realtors
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None


class RealtorView(RetrieveAPIView):
    #  display a single realtor details
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
