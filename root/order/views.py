from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order, CartItem
from .serializers import OrderSerializer, CartItemSerializer
from .permissions import GetOnly

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user,status="pending")


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(order__user=self.request.user, order__status='pending')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        order = instance.order

        tempPrice = instance.quantity * instance.price_at_purchase

        order.total_price -= tempPrice

        order.save()

        return super().destroy(request, *args, **kwargs)


class OrderHistoryViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [GetOnly]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).exclude(status="pending")