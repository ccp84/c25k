from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run, Profile, User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    run_list = Run.objects.all().order_by('-date')
    context = {
        "run_list": run_list
    }
    return render(request, 'home.html', context)


class RunList(ListView):

    model = Run


class RunCreate(SuccessMessageMixin, CreateView):
    model = Run
    template_name = 'run_create.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
    success_message = "Run created"


class RunUpdate(SuccessMessageMixin, UpdateView):
    model = Run
    template_name = 'run_update.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
    success_message = "Run updated"


class RunDelete(SuccessMessageMixin, DeleteView):
    model = Run
    template_name = 'run_delete.html'
    success_url = '/run/list'
    success_message = "Run deleted"


def run_join(request, pk):
    run = get_object_or_404(Run, id=pk)

    if run.runners.filter(id=request.user.id).exists():
        run.runners.remove(request.user)
        messages.add_message(request, messages.INFO, 'You have been removed from the run list')
    else:
        run.runners.add(request.user)
        messages.add_message(request, messages.INFO, 'You have been added to the run list')

    return HttpResponseRedirect(reverse('run_list'))
