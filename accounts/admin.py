from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 기존의 User과 비슷하게 만들어준다.
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)