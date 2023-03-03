from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run, Profile, User
from datetime import datetime, timedelta


def home(request):
    run_list = Run.objects.all().order_by('-date')
    context = {
        "run_list": run_list
    }
    return render(request, 'home.html', context)


class RunList(ListView):
    model = Run


class RunCreate(CreateView):
    model = Run
    template_name = 'run_create.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'


class RunUpdate(UpdateView):
    model = Run
    template_name = 'run_update.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
