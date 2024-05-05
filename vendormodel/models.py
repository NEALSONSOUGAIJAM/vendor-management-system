from django.db import models
from django.db.models import Count, Avg
from django.utils import timezone
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    
    def update_performance_metrics(self):
        # Update on-time delivery rate
        completed_orders = self.purchase_orders.filter(status='completed')
        total_completed_orders = completed_orders.count()
        on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        self.on_time_delivery_rate = (on_time_orders / total_completed_orders) * 100 if total_completed_orders else 0

        # Update quality rating average
        self.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

        # Update average response time
        response_times = completed_orders.exclude(acknowledgment_date=None).annotate(
            response_time=models.ExpressionWrapper(models.F('acknowledgment_date') - models.F('issue_date'),
                                                   output_field=models.DurationField())
        ).aggregate(Avg('response_time'))['response_time__avg']
        self.average_response_time = response_times.total_seconds() if response_times else 0

        # Update fulfillment rate
        total_orders = self.purchase_orders.count()
        successful_orders = self.purchase_orders.filter(status='completed').count()
        self.fulfillment_rate = (successful_orders / total_orders) * 100 if total_orders else 0

        # Save the updated performance metrics
        self.save()