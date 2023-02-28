from django.db import models
from django.contrib.auth.models import User


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
        ordering = ['-date']

    def __str__(self):
        return self.title + self.date

    def num_of_runners(self):
        return self.runners.count()
