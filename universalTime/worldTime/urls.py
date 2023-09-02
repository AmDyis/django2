from django.urls import path

from .views import *

urlpatterns = [
    path('HI2/', index),
    path('about/', about),

]