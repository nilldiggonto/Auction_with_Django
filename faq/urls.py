from django.urls import path
from .views import q_a_faq

app_name = 'faq'

urlpatterns = [
    path('',q_a_faq,name='faq'),
]
