from django.contrib import admin
from django.urls import path
import uuid
from rest_framework import routers
from .views import UserAPIView, UserListView, UserRUDView

app_name = 'users'
router = routers.SimpleRouter()

router.register('create', UserAPIView, 'users')

urlpatterns = tuple(router.urls)
urlpatterns += (
    path('', UserListView.as_view(), name = 'user-list'),
    path('<uuid:pk>', UserRUDView.as_view(), name='user-rud'),
)