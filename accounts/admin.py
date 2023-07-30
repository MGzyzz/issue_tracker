from django.contrib import admin
from accounts.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name', 'username', 'date_joined', 'last_login', 'is_superuser']
    list_filter = ['id', 'first_name', 'last_name', 'username', 'password']


admin.site.register(User, UserAdmin)
