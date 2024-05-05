from django.urls import path
from .views import VendorListCreateView,VendorRetrieveUpdateDestroyView, VendorPerformanceView

urlpatterns = [
    path('vendors/',VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/',VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
     path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]
