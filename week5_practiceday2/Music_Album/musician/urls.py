from django.urls import path, include
from . import views

urlpatterns = [
    path("add/", views.AddMusicianClass.as_view(), name="add_musician"),
]
