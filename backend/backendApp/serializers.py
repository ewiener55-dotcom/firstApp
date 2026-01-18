from rest_framework import serializers
from .models import RateActivity

class RateActivitySerializer(serializers.ModelSerializer):
    Image = serializers.ImageField(use_url=True)
    class Meta:
        model = RateActivity
        fields = ['id','Title','Image','Rating','Created_on']
        read_only_fields = ['id','Created_on']
