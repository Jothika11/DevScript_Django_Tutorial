from django.urls import path
from .views import*

urlpatterns = [
    path("person/<str:person>",hey),
    path('',index,name='home'),
    path('form',get_name, name='form')
]