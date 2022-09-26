from django.urls import path

from playground import s3dictionary
from . import views

#URLConfig
urlpatterns = [
    path('',views.say_hello),
    path('s3/',views.s3RequestHandler)
]
