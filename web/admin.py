from django.contrib import admin

# Register your models here.
from .models import Item, Comment, User, Images

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Images)