from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room,  on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text







