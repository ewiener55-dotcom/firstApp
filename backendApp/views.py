from django.shortcuts import render
from rest_framework import generics
from .serializers import RateActivitySerializer
from .models import RateActivity
# Create your views here.

class ViewRateActivity(generics.ListCreateAPIView):
    queryset = RateActivity.objects.all()
    serializer_class = RateActivitySerializer
class ViewRateActivityCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RateActivity.objects.all()
    serializer_class = RateActivitySerializer