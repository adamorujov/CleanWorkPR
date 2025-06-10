from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from core.models import Banner
from core.api.serializers import BannerSerializer, BannerRetrieveSerializer

class BannerListCreateAPIView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerRetrieveSerializer
    lookup_field = "id"

class BannerDestroyAPIView(DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = "id"
