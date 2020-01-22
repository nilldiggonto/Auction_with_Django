from django.urls import path
# from .views import TweetListApiView,TweetCreateApiView
from .views import bid_create
app_name = 'api'

urlpatterns = [
    path('create/',bid_create,name='api-create'),
    # path('',TweetListApiView.as_view(),name='api-list'),
    # path('create/',TweetCreateApiView.as_view(),name='api-create'),
]