from rest_framework.decorators import api_view
from .serializers import LiveAuctionserializerBid
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response






@api_view(['POST'])
def bid_create(request):
    if request.method == 'POST':
        serializer = LiveAuctionserializerBid(data= request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)