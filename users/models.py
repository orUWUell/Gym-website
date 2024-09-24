from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(default="profile.jpg", null=True, blank=True,
                                        upload_to='images/profile_pictures')



