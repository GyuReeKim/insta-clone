from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser): # AbstractUser를 상속받았다.
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")