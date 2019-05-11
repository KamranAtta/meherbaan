from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Expense(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, unique = True, max_length=255)
    school = models.OneToOneField('school.School', on_delete=models.CASCADE, null=True)
    fee = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    books = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    uniform = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    shoes = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    transport = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    lunch = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    date_created = models.DateTimeField(blank=True, null=True, editable=False,
                                        auto_now_add=True,
                                        verbose_name=_('date created'))
    date_modified = models.DateTimeField(blank=True, null=True, editable=False,
                                         auto_now=True,
                                         verbose_name=_('date modified'))

    def __str__(self):
        return self.school.name

    def school_name(self):
        return self.school.name

    def total_amount(self):
        return self.fee + self.books + self.uniform + self.shoes + self.transport + self.lunch
