from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . import forms
from .models import Musician


# Create your views here.


class AddMusicianClass(CreateView):
    model = Musician
    form_class = forms.musicianForm
    template_name = "add_musician.html"
    success_url = reverse_lazy("add_musician")
