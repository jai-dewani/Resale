from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('signupuser',views.signupview,name='signupuser'),
    path('loginuser',views.loginview,name='loginuser'),
    path('logoutuser',views.logoutview,name='logoutuser'),
    
]