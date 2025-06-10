from django.urls import path
from core.api import views

urlpatterns = [
    path('banner-list-create/', views.BannerListCreateAPIView.as_view()),
    path('banner-retrieve-update/<int:id>/', views.BannerRetrieveUpdateAPIView.as_view()),
    path('banner-destroy/<int:id>/', views.BannerDestroyAPIView.as_view())
]