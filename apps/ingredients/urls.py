from django.urls import path

from .views import create_ingredient, index

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_ingredient, name="create_ingredient"),
]
