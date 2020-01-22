
from rest_framework import serializers
from live_auction.models import Product_price_live
# from accounts.api.serializers import UserDispalySerializer
class LiveAuctionserializerBid(serializers.ModelSerializer):
    # user = UserDispalySerializer(read_only=True)
    class Meta:
        model = Product_price_live
        fields = [
            
            'bid_price',
        ]