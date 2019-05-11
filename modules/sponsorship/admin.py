from django.contrib import admin
from modules.sponsorship.models import Sponsorship


class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('relation','expense','donation','duration','is_active','date_modified')

admin.site.register(Sponsorship, SponsorshipAdmin)
