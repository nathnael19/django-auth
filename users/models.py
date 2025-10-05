from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    objects = UserManager()

    def __str__(self):
        return self.email