from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=10, default='1st')
    phoneNumber = models.CharField(max_length=20)
    profilepicture = models.ImageField()

    def __str__(self):
        return self.username


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    itemImage = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.itemName


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.comment
