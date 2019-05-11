from calendar import timegm
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from modules.users.api.user import helpers as user_helpers
from django.conf import settings
import jwt




def jwt_payload_handler(user):
    return {
        'user_id': str(user.pk),
        'username': user.email,
        'email_address': user.username,
        'exp' : datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'orig_iat': timegm(datetime.utcnow().utctimetuple()
        ) 

    }

def jwt_login_only_verified_user(user):
    if not user_helpers.user_is_verified(user.pk):
        return {
            'error': 'Please verify your email address'
        }
    return True

def jwt_response_payload_handler(token, user=None, request=None):
    verified = jwt_login_only_verified_user(user)
    if verified == True:
        decoded_values = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return {
            'token': token,
            'user_id': decoded_values['user_id'],
            'username': decoded_values['email_address'],
            'email_address': decoded_values['username'],
            'verified': verified
        }
    return verified

