from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("add/", views.AddAlbumClass.as_view(), name="add_album"),
    path("edit/<int:id>/", views.edit.as_view(), name="edit"),
    path("delete/<int:id>/", views.delete.as_view(), name="delete"),
]
