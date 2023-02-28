from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Run


class RunList(ListView):
    model = Run
    queryset = Run.objects.all().order_by('-date')
    template = 'home.html'
