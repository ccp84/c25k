from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


USER_TYPE = ((0, 'Runner'), (1, 'Leader'))


class Run(models.Model):
    title = models.CharField(max_length=80)
    leader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='run_leader')
    location = models.CharField(max_length=100)
    date = models.DateField(help_text='DD/MM/YYYY')
    time = models.TimeField(help_text='HH:MM')
    details = models.TextField(blank=True)
    runners = models.ManyToManyField(
        User, related_name='run_signup', blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title + str(self.date)

    def num_of_runners(self):
        """
        Function to return the number
        of runners signed up to a run
        """
        return self.runners.count()

    def signed_up(self):
        """
        Function to check if a runner's id
        is in the list of runners signed up for
        a run.
        """
        name_list = []
        runner_list = self.runners.all()
        for runner in runner_list:
            name_list.append(runner.id)
        return name_list

    def take_register(self):
        """
        Function to return the list of names of
        runners who have signed up for a run.
        """
        register = []
        runner_list = self.runners.all()
        for runner in runner_list:
            register.append([runner.first_name, runner.last_name, runner.id])
        return register


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile')
    DOB = models.DateField(blank=True, null=True)
    ICE = models.CharField(max_length=20, blank=True)
    medical = models.TextField(blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.first_name
