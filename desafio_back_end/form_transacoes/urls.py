from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("save_file_content", views.save_file_content, name="save_file_content"),
]
