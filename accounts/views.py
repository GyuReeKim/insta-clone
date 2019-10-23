from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아닌 Form을 상속하므로 Custom이 필요없다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

def user_page(request, id):
    # 기본적으로 django에서 제공하는 user와의 충돌을 피하기 위해서 user_info로 변경하였다.
    user_info = get_object_or_404(User, id=id)
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/user_page.html', context)