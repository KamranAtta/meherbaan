from django.contrib import admin
from django.urls import path
import uuid
from rest_framework import routers
# from .views import SponsorshipAPIView, SponsorshipRUDView
#
# app_name = 'sponsorship'
# router = routers.SimpleRouter()
#
# # router.register('create', UserAPIView, 'users')
#
# # urlpatterns = tuple(router.urls)
# urlpatterns += (
#     path('', SponsorshipAPIView.as_view(), name = 'sponsorship-list'),
#     path('<uuid:pk>', SponsorshipRUDView.as_view(), name='sponsorship-rud'),
# )
