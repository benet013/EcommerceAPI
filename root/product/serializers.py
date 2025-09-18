from rest_framework import serializers
from order.models import Order
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  
        write_only=True
    )
    available_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product 
        fields = ['id','name','description','price','stock','available_stock','image','category','category_id']

    def get_available_stock(self, obj):
        user=self.context['request'].user
        orders = Order.objects.filter(user=user).exclude(status="pending")
        tempQty = 0
        for order in orders:
            for item in order.orderitems.all():
                # print("Item:", item.product.id, item.quantity)
                if obj.id == item.product.id:
                    tempQty += item.quantity

        return max(obj.stock-tempQty,0)
      
