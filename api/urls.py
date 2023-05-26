from django.urls import path,include
from .views import Home,Search




urlpatterns = [
    path("home", Home.as_view()),
    path("search", Search.as_view()),
]