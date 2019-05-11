from django.contrib import admin
from modules.users.models import User, Guardian, Admin, Student, Relation
from django.contrib.auth.admin import UserAdmin as user_admin

class UserAdmin(user_admin):
    fieldsets = None
    pass

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','age','gender','detail','education','blood_group','hobbies')

class GuadianAdmin(admin.ModelAdmin):
    list_display = ('user','address','occupation','cnic','date_created')

class RelationAdmin(admin.ModelAdmin):
    list_display = ('guardian','student','date_created','date_modified')

admin.site.register(User,UserAdmin)
admin.site.register(Guardian, GuadianAdmin)
admin.site.register(Admin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Relation, RelationAdmin)

