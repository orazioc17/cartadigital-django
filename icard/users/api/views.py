from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password

from ..models import User
from .serializers import UserSerializer


class UserApiViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Haciendo override del create para que encripte el password del usuario
        """
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, *kwargs)
