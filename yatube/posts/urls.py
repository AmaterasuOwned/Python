from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path("", views.index),
    # Страница со списком постов
    path("posts/", views.posts_list),
    # Посты от группы
    path("group/<slug:pk>/", views.group_posts),
]
