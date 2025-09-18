from decimal import Decimal
from rest_framework import serializers
from .models import Order,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
        read_only_fields = ['order']

    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.filter(user=user,status="pending").first()

        if order is None:
            order = Order.objects.create(user=user)
            
        validated_data['order'] = order

        orderitem = CartItem.objects.create(**validated_data)

        order.save()
        return orderitem
    
            

class OrderSerializer(serializers.ModelSerializer):
    orderitems = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order 
        fields = ['id','user','total_price', 'status', 'orderitems']


