from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(AbstractUser):
    userProfile=models.ImageField(upload_to="user")
    type = models.CharField(max_length=20)


class Category(models.Model):

    title =models.CharField(max_length=200)

    description = models.TextField()

    def __str__(self):
        return self.title
    

class addGround(models.Model):
    owner_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    box_name = models.CharField(max_length=100)
    location = models.TextField()
    timings  = models.TextField()
    image    = models.ImageField(upload_to='user')
    price    = models.CharField(max_length=5, default="1000")

class booking(models.Model):
    user_id    = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=1)
    ground_id  = models.ForeignKey(addGround,on_delete=models.CASCADE,default=1)
    sports     = models.CharField(max_length=30,default="cricket")
    day        = models.DateField()
    time       = models.CharField(max_length=10, default="3 PM")
    hours      = models.CharField(max_length=2, default="1")
    