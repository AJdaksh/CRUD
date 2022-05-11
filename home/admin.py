from django.contrib import admin
from .models import user,signup,task
# Register your models here.
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','mobile','Description')

@admin.register(signup)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Username','email','password')

@admin.register(task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('tasktitle','duedate','status','description')


