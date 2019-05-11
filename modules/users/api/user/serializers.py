from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from modules.users.api.user import helpers as user_helpers
from modules.users.models import User

class NewUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=30)
    password1 = serializers.CharField(required=True, min_length=6)
    password2 = serializers.CharField(required=True, min_length=6)
    first_name = serializers.CharField(required=False, max_length=30, default='')
    last_name = serializers.CharField(required=False, max_length=30, default='')
    email = serializers.EmailField(required=True)

    def validate_username(self, value):
       user_obj = user_helpers.user_get_by_name(value)
       if user_obj is not None:
           raise serializers.ValidationError('Username taken.')
       return value

    def validate_email(self, value):
       user_obj = user_helpers.user_get_by_email_address(value)
       if user_obj is not None:
           raise serializers.ValidationError('Email has already been used by another')
       return value

    def create(self, validated_data):
       user = user_helpers.user_create(
           username=self.validated_data['username'],
           password=self.validated_data['password1'],
           first_name=self.validated_data.get('first_name'),
           last_name=self.validated_data.get('last_name'),
           email=self.validated_data['email'],
       )
       return user

    def validate(self, data):
       if 'password1' in data and 'password2' in data:
           if data['password1'] != data['password2']:
               raise serializers.ValidationError(
                   _('The passwords do not match.')
               )
       return data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ['id']