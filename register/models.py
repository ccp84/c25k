from django.db import models
from django.contrib.auth.models import User


USER_TYPE = ((0, 'Runner'), (1, 'Leader'))


class Run(models.Model):
    title = models.CharField(max_length=80)
    leader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='run_leader')
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    details = models.TextField(blank=True)
    runners = models.ManyToManyField(
        User, related_name='run_signup', blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title + self.date

    def num_of_runners(self):
        return self.runners.count()


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    DOB = models.DateField()
    ICE = models.CharField(max_length=20)
    medical = models.TextField()
    user_type = models.IntegerField(choices=USER_TYPE, default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} | Status: {self.user_type}"

    def toggle_status(self):
        if self.user_type == 0:
            self.user_type = 1
            return f"{self.first_name} is now set as a run leader"
        elif self.user_type == 1:
            self.user_type = 0
            return f"{self.first_name} is now set as a runner"
        else:
            return "Invalid user type set"

    def toggle_completed(self):
        pass
