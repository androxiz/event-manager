from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=256, blank=True)
    date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=128, blank=True)
    organizer = models.ForeignKey(User, on_delete = models.CASCADE, null=False)
    participants = models.ManyToManyField(User,  related_name='registred_events', blank = True)

    def __str__(self):
        return f'{self.title}: {self.date}'