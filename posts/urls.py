from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('hashtags/<int:id>/', views.hashtags, name="hashtags"),
    path('<int:id>/like/', views.like, name="like"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('feed/', views.feed, name="feed"),
    path('<int:id>/detail/like/', views.detail_like, name="detail_like"),
    path('all/', views.all, name="all"),
]
