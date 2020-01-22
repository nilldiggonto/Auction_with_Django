from django.urls import path
from .views import billing,billing_address,billing_edit

app_name = 'billing'

urlpatterns = [
    path('',billing,name='bill'),
    path('address/',billing_address,name='address'),
    path('<int:id>/address/update/',billing_edit,name='update'),
]
