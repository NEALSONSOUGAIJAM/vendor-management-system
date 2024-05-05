from django.contrib import admin
from .models import PurchaseOrder,HistoricalPerformance

admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)
