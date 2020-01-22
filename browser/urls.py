from django.urls import path,include
from .views import item_list,item_detail,item_create,userprofile,bidder_detail,category_post,item_category,contact_page,bidding_item_log
from django.conf import settings
from django.conf.urls.static import static

app_name= 'browse'
urlpatterns = [
    path('',item_list,name='item_index'),
    path('create/',item_create,name='item_create'),
    path('account/',userprofile,name='account'),
    path('bidder/',bidder_detail,name='bidder'),
    path('bidlog/',bidding_item_log,name='bid-log'),
    path('category/',item_category,name='category-list'),
    path('contact/',contact_page,name='contact'),
    # path('bidder/<int:pk>/',bidder_detail,name='bidder'),
    
    path('<str:slug>/',item_detail,name='item_detail'),
    

    
    path('category/<str:slug>/',category_post,name='category'),
    
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
