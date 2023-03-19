from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Run, Profile, User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm, RunForm, ProfileUpdateForm


def home(request):
    run_list = Run.objects.all().order_by('date')
    context = {
        "run_list": run_list
    }
    return render(request, 'home.html', context)


class RunList(ListView):

    model = Run
    template_name = 'run_list.html'


class RunCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Run
    template_name = 'run_create.html'
    form_class = RunForm
    success_url = '/run/list'
    success_message = "Run created"


class RunUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Run
    template_name = 'run_update.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
    success_message = "Run updated"


class RunDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Run
    template_name = 'run_delete.html'
    success_url = '/run/list'
    success_message = "Run deleted"


def run_join(request, pk):
    run = get_object_or_404(Run, id=pk)

    if run.runners.filter(id=request.user.id).exists():
        run.runners.remove(request.user)
        messages.add_message(
            request, messages.INFO, 'You have been removed from the run list')
    else:
        run.runners.add(request.user)
        messages.add_message(
            request, messages.INFO, 'You have been added to the run list')

    return HttpResponseRedirect(reverse('run_list'))


class ProfileCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile_create.html'
    form_class = ProfileForm
    success_url = '/profile'
    success_message = "Profile Updated"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        profile = Profile.objects.filter(user__id=request.user.id)

        return render(request, 'profile.html', {'profile': profile})


class ProfileUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    form_class = ProfileUpdateForm
    success_url = '/profile'
    success_message = 'Profile Updated'

    def get_queryset(self):
        query_set = Profile.objects.filter(user=self.request.user)
        return query_set


class ProfileDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = '/profile'
    success_message = "Profile Deleted"

    def get_queryset(self):
        query_set = Profile.objects.filter(user=self.request.user)
        return query_set


class RunnerProfile(View):

    def get(self, request, id):
        runner = Profile.objects.filter(user__id=id)
        # is_leader = False
        # if runner.user.groups.filter(name="leader").exists():
        #     is_leader = True
        context = {
            "runner": runner
        }

        return render(request, 'runner_profile.html', context)
