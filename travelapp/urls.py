from django.urls import path
from . import views
from .views import about

urlpatterns=[
    path('',views.fun,name='fun'),
    path('about', views.about, name="about"),

]