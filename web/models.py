from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=10, default='1st')
    phoneNumber = models.CharField(max_length=20)
    profilepicture = models.ImageField(upload_to='profilePicture')

    def __str__(self):
        return self.username


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    itemImage = models.FileField(upload_to='items')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.itemName

class Images(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items')

    def __str__(self):
        return self.item


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.comment
