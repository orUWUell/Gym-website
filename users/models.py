from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(default="profile.jpg",
                                        upload_to='images/profile_pictures')
    description = models.TextField(default='There could be your description', max_length=150)



