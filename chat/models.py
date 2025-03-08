from django.contrib.auth import get_user_model
from django.db import models
import os
from PIL import Image

from django.contrib.postgres.fields import ArrayField



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


class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.TextField()
    room = models.ForeignKey(Room,  on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/message_pictures', blank=True, null=True)

    @property
    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)
        else:
            return None

    def __str__(self):
        if self.text:
            return f'{self.author.username} : {self.text}'
        elif self.file:
            return f'{self.author.username} : {self.filename}'

    @property
    def is_image(self):
        try:
            image = Image.open(self.file)
            image.verify()
            return True
        except:
            return False








