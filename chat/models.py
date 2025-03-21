from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class File(models.Model):
    file = models.FileField(upload_to='files/', blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.file_name

class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.TextField()
    likes = models.IntegerField(default=0)
    room = models.ForeignKey(Room,  on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text









