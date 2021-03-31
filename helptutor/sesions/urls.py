from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
]