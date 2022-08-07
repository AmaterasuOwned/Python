from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path(
        "",
        views.index,
    ),
    path("posts/", views.posts_list, name="posts_list"),
    path("group/", views.group_posts, name="group_list"),
]
