from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run, Profile, User


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


class RunDelete(DeleteView):
    model = Run
    template_name = 'run_delete.html'
    success_url = '/run/list'


def run_join(request, pk):
    run = get_object_or_404(Run, id=pk)

    if run.runners.filter(id=request.user.id).exists():
        run.runners.remove(request.user)
    else:
        run.runners.add(request.user)

    return HttpResponseRedirect(reverse('run_list'))
