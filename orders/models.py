from django.db import models
from django.contrib.auth.models import User
from products.models import Item

# Create your models here.

ORDER_STATUS_CHOICES = [
    ('PENDING','Pending'),
    ('IN_PROGRESS','In Progress'),
    ('DELIVERED','Delivered'),
    ('CANCELLED','Cancelled'),
]

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(Item)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES,default = 'PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Order #{self.id}-{self.customer.username}"
