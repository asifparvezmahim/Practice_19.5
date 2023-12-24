from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AddAlbumClass(CreateView):
    model = models.Album
    form_class = forms.albumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("add_musician")


class edit(UpdateView):
    model = models.Album
    form_class = forms.albumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("homepage")
    pk_url_kwarg = "id"


# def delete(request, id):
#     album = models.Album.objects.get(pk=id)
#     album.delete()
#     return redirect("homepage")


class delete(DeleteView):
    model = models.Album
    template_name = "delete.html"
    success_url = reverse_lazy("homepage")
    pk_url_kwarg = "id"
