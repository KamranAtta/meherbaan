from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django import forms


# Create your models here.
class Sponsorship(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, unique = True, max_length=255)
    relation = models.ForeignKey('users.Relation',on_delete=models.CASCADE, null=True)
    expense = models.ForeignKey('expense.Expense',on_delete=models.CASCADE, null=True)
    donation = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False, verbose_name=_('active'))
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now_add=True,
                                        verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                         auto_now=True,
                                         verbose_name=_('date modified'))


    def __str__(self):
        return str(self.relation)
