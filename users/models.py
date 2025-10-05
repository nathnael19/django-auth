from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','phone']

    def __str__(self):
        return self.username