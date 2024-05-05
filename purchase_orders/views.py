from django.shortcuts import render
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer
# Create your views here.

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



class HistoricalPerformanceListCreateView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

