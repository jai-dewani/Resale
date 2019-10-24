from django.contrib import admin

# Register your models here.
from .models import Item, Comment, UserAccount, Image

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(UserAccount)
admin.site.register(Image)