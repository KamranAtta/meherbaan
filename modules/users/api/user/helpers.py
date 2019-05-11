from modules.users.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import transaction


def validate(data):
    if data['password1'] != data['password2']:
        raise serializers.ValidationError(_('THe passwords do not match'))

def user_get_by_name(username):
    try:
        return User.objects.get(username=username)
    except:
        return None

def user_get_by_email_address(email):
    try:
        return User.objects.get(email=email)
    except:
        return None

def validate_email(email):
    try:
        return User.objects.get(email=email)
    except:
        return None

def user_is_verified(user_id):
        try:
                return User.objects.get(id=user_id)
        except:
                return None

@transaction.atomic
def user_create(username,password, first_name, last_name, email):
    if email:
        email = email.lower()
    m = User(username=username, first_name=first_name, last_name=last_name, email=email)
    m.set_password(password)
    m.save()

    return m


