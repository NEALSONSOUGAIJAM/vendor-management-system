from django.urls import path
from .views import (PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView,
    HistoricalPerformanceListCreateView, HistoricalPerformanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('historical_performance/', HistoricalPerformanceListCreateView.as_view(), name='historical-performance-list-create'),
    path('historical_performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDestroyView.as_view(), name='historical-performance-retrieve-update-destroy'),
]