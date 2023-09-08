from customers.views import UserViewSet
from rest_framework import routers
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]