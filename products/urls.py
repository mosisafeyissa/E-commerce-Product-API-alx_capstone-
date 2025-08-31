from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet, OrderViewSet, CategoryViewSet

# DRF Router
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]