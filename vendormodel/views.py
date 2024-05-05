from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
#from .utils import calculate_vendor_performance_metrics
from rest_framework import status


# Create your views here.
# Git commit check



class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    