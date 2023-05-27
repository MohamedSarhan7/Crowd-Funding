from django.urls import path,include
from .views import *




urlpatterns = [
    path("home", Home.as_view()),
    path("search", Search.as_view()),
    path("categories", CategoryList.as_view()),
    path("tags", TagList.as_view()),
    path("projects", ProjectList.as_view()),
    path("projects/<int:id>", ProjectDetail.as_view()),
]