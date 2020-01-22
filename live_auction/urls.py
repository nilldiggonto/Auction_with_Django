from django.urls import path
from .views import live_auctionlist, live_aution_create,live_auction_detail,live_auctionlist_user,bidder_detail_live,bidding_item_log_live
app_name ='live'
urlpatterns = [

    path('',live_auctionlist,name='live-list'),
    path('go-live/',live_aution_create,name='live-create'),
    path('live-user/',live_auctionlist_user,name='live-user'),
    path('live-bidder-detail/',bidder_detail_live,name='bid-user-detail'),
    path('live-bid-log/',bidding_item_log_live,name='live-user-bid-log'),
    path('live/<str:slug>/',live_auction_detail,name='live-detail'),

]