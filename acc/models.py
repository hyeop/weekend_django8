from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    comment = models.TextField()
    pic = models.ImageField() # pip install pillow 
    point = models.IntegerField(default=0)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"
    

