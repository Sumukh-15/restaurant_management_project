from rest_framework import serializers
from .models import Order
from products.models import Item

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,queryset= Item.objects,all()
    )
    class Meta:
        model = Order
        fields = "__all__"