from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from ..models import User
from .serializers import UserSerializer


class UserApiViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
