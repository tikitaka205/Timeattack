from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = 'user'  # 유저 테이블
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=10, blank=True)
