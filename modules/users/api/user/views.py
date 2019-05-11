#from django.contrib.auth.models import User
from modules.users.models import User
from django.db import transaction
from rest_framework.response import Response
from .serializers import NewUserSerializer, UserSerializer
from rest_framework import generics, mixins, viewsets, status

class UserAPIView(viewsets.ViewSet):
    # NON JWT VIEW 
    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = NewUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_obj = serializer.create(serializer.validated_data)
        response = {
            'user_id': user_obj.pk,
            'username': user_obj.username,
            'email': user_obj.email
        }
        return Response(response, status=status.HTTP_201_CREATED)


class UserListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

