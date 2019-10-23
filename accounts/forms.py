from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # 상속이 필요하다.
        model = User
        # fields = UserCreationForm.Meta.fields + 