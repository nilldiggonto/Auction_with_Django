from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . views import (dashboard,product_view,product_detail,product_category,
                        contact_admin_all,contact_admin_detail,contact_admin_read,
                        contact_admin_unread,all_bid,bid_detail,winning_bid,bid_win_loss,
                        live_product_view,live_product_detail,all_live_bid,all_premium,user_view,
                        user_active_view,active_address,)
app_name = 'nilam_admin'

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('user/',user_view,name='user_view'),
    path('product/',product_view,name='product'),
    path('product/category',product_category,name='product_category'),
    path('contact/admin/all/',contact_admin_all,name='all'),
    path('contact/admin/read/',contact_admin_read,name='read'),
    path('contact/admin/unread/',contact_admin_unread,name='unread'),
    path('all/bid/',all_bid,name='all_bid'),
    path('all/winning/',winning_bid,name='win_bid'),
    path('live/product/',live_product_view,name='live_product'),
    path('live/bid/all/',all_live_bid,name='live_bid'),
    path('live/bid/all/premium/',all_premium,name='premium'),
    path('user/active/',user_active_view,name='user_active'),

    path('product/<str:slug>/',product_detail,name='product_detail'),
    path('live/product/<str:slug>/',live_product_detail,name='live_detail'),
    path('contact/admin/detail/<str:slug>/',contact_admin_detail,name='detail'),


    path('bid/<int:pk>/',bid_detail,name='bid_detail'),
    path('active/address/<int:id>/',active_address,name='active_add'),
    path('bid/win/loss/<str:slug>/',bid_win_loss,name='bid_win_loss'),


    
]
