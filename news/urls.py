from django.contrib import admin
from django.urls import path
from .views import PostList, PostDetail, Posts, SearchView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('posts/', Posts.as_view()),
    path('search/', SearchView.as_view()),
]
