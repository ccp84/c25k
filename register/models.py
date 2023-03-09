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
        return self.runners.count()

    def signed_up(self):
        name_list = []
        runner_list = self.runners.all()
        for runner in runner_list:
            name_list.append(runner.id)
        return name_list

    def take_register(self):
        register = []
        runner_list = self.runners.all()
        for runner in runner_list:
            register.append([runner.first_name, runner.last_name])
        return register


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile')
    DOB = models.DateField(blank=True, null=True)
    ICE = models.CharField(max_length=20, blank=True)
    medical = models.TextField(blank=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=0, blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.first_name

    def toggle_status(self):
        if self.user_type == 0:
            self.user_type = 1
            return f"{self.user.first_name} is now set as a run leader"
        elif self.user_type == 1:
            self.user_type = 0
            return f"{self.user.first_name} is now set as a runner"
        else:
            return "Invalid user type set"

    def toggle_completed(self):
        pass
