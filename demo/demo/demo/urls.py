from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views

from appin import views 

urlpatterns = [
    path('admin/', admin.site.urls),
  
    
    path("",views.home,name="home"),
    path("register",views.register,name="register"),

]