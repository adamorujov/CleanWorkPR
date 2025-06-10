from rest_framework import serializers
from core.models import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("title", 'image')

class BannerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
