from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts_list, name="posts_list"),
    path("group/<slug:slug>", views.group_posts, name="group_posts"),
]
