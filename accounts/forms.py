from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # 상속이 필요하다.
        model = User
        # fields = UserCreationForm.Meta.fields + 

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # model = setting.Auth_User_MODEL # 'accounts.user' 문자열 형식이다.
        model = get_user_model() # User 클래스
        fields = ('email', 'first_name', 'last_name',)