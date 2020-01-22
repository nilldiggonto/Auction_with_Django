from django.urls import  path
from .views import checkout,checkout_create
app_name = 'checkout'
urlpatterns = [
    path('',checkout,name='check'),
    path('create/',checkout_create,name='c_create'),
]