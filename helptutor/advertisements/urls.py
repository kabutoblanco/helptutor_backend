from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from helptutor.advertisements.api import *

router = DefaultRouter()
router.register('advertisement', AdvertisementViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/student/<int:pk>/advertisement/', StudentAdvertisementAPIView.as_view()),
    path('api/advertisement/<int:pk>/answer/', AdvertisementAnswerAPIView.as_view()),
]
