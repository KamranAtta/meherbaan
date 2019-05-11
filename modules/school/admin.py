from django.contrib import admin
from modules.school.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact','city','country','date_modified')

admin.site.register(School, SchoolAdmin)

