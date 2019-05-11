from django.contrib import admin
from modules.residence.models import Residence


class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact','city','country','warden','date_modified')

admin.site.register(Residence, ResidenceAdmin)