from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserApiViewset


router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewset
)
