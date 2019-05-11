from __future__ import unicode_literals

from django.db import models
import uuid
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
    )
# from modules.residence.models import Residence
# from modules.school.models import School
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password,False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        username = ''

        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password,True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    def setup_guardian(user):
        Guardian.objects.create(
            user=user,
        )

    def setup_student(user):
        Student.objects.create(
            user=user
        )

    ROLES = {
        0: setup_guardian,
        1: setup_student
    }

    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True, editable=False )
    username = models.CharField(null=True, blank=True, max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    role = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    is_staff = models.BooleanField(
       _('staff status'),
       default=False,
       help_text='Designates whether the user can log into this admin site.',
   )
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                       auto_now_add=True,
                                       verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now=True,
                                        verbose_name=_('date modified'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def clean(self):
        self.username = self.username.lower()

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Admin(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                       auto_now_add=True,
                                       verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now=True,
                                        verbose_name=_('date modified'))

    def __str__(self):
        return self.user.username

class Guardian(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    address = models.CharField(max_length=255, blank=True, null=True)
    image  = models.ImageField(upload_to='images/gardians/', null=True, blank=True)
    occupation = models.CharField(max_length=30)
    cnic = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                       auto_now_add=True,
                                       verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now=True,
                                        verbose_name=_('date modified'))

    def __str__(self):
        return self.user.username

class Student(models.Model):
    GENDER = (
        ('MALE','Male'),
        ('FEMALE', 'Female'),
        ('Other', 'Other'),
    )
    id = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, )
    residence = models.ForeignKey('residence.Residence', on_delete=models.CASCADE,null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, default='Female', max_length=20)
    image  = models.ImageField(upload_to='images/students/', null=True, blank=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    ambition = models.CharField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=30, verbose_name='blood group', blank=True, null=True)
    hobbies = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                       auto_now_add=True,
                                       verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now=True,
                                        verbose_name=_('date modified'))
    def __str__(self):
        return self.user.username

class Relation(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True, default=uuid.uuid4, editable=False, )
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                       auto_now_add=True,
                                       verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now=True,
                                        verbose_name=_('date modified'))

    def __str__(self):
        return self.guardian.user.username + ' ' + self.student.user.username
