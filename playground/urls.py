from django.urls import path

from playground import s3dictionary
from . import views

#URLConfig
urlpatterns = [
    path('hello/',views.say_hello),
    path('',views.s3RequestHandler)
]
