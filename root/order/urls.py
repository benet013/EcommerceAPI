from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CartItemViewSet, OrderHistoryViewSet


router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')
router.register(r'cart', CartItemViewSet, basename='cart')
router.register(r'orderhistory', OrderHistoryViewSet, basename="orderhistory")

urlpatterns = router.urls