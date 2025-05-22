from django.urls import path ,include
from .views import *


urlpatterns=[
    path('home/',homepage)
]


urlpatterns=[
    path('',views.home , name ='home')
]