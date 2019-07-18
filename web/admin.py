from django.contrib import admin

# Register your models here.
from .models import Item, Comment, User

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(User)