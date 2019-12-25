from django.contrib import admin

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','email','gender','phone','c_time','u_time')
    list_filter = ('gender',)
    search_fields = ('username','phone','email')

admin.site.register(User,UserAdmin)