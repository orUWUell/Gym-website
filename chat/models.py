from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Room(models.Model):
    genres = (
        ('Technology', 'Technology'),
        ('Science', 'Science')
            )

    name = models.CharField(max_length=255)
    question = models.TextField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)




    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room,  on_delete=models.CASCADE)

    def __str__(self):
        return self.text







