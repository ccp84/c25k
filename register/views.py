from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Run
from datetime import datetime, timedelta


def home(request):
    run_list = Run.objects.all().order_by('-date')
    context = {
        "run_list": run_list
    }
    return render(request, 'home.html', context)


class RunList(ListView):
    model = Run
