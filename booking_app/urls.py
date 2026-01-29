from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RegionListAPIView, RegionDetailAPIView, CityListAPIView, CityDetailAPIView, PropertyListAPIView, PropertyDetailAPIView,
    PropertyImageViewSet, ReviewViewSet, UserProfileViewSet)

router = DefaultRouter()
router.register(r'property-images', PropertyImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view()),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view()),
    path('country/', RegionListAPIView.as_view()),
    path('country/<int:pk>/', RegionDetailAPIView.as_view()),
    path('city/', CityListAPIView.as_view()),
    path('city/<int:pk>/', CityDetailAPIView.as_view()),
]
