from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet


router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = router.urls