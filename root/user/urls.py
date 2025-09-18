from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet

router = DefaultRouter()
router.register(r'',RegisterViewSet)

urlpatterns = router.urls