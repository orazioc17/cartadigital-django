from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Indicando que el email sera unico
    email = models.EmailField(unique=True)

    # Indicando que el field para iniciar sesion en admin es el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
