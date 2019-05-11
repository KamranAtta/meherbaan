from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from modules.expense.models import Expense

# Create your models here.
class School(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, unique = True, max_length=255)
    name = models.CharField(max_length=100,  default = "")
    address =  models.CharField(max_length=100, blank=True, null=True)
    contact =  models.CharField(max_length=100, blank=True, null=True)
    city =  models.CharField(max_length=100, blank=True, null=True)
    country =  models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now_add=True,
                                        verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                         auto_now=True,
                                         verbose_name=_('date modified'))

    def __str__(self):
        return self.name
