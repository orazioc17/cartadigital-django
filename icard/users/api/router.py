from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserApiViewset, UserView


router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewset
)

urlpatterns = [
    path('auth/me/', UserView.as_view()),
]