from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class UserAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=10, default='1st')
    phoneNumber = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    profilepicture = models.ImageField(upload_to='profilePicture',blank=True)
    
    def __str__(self):
        return self.username


class Item(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    posted_at = models.DateTimeField(default=datetime.now(), blank=True)
    
    def __str__(self):
        return self.itemName

class Image(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items')

    def __str__(self):
        return self.item.itemName


class Comment(models.Model):
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.comment
