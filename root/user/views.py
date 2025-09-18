from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer

class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer