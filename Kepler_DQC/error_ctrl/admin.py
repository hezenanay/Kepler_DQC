from django.contrib import admin

# Register your models here.

from .models import Error_task
class ErrortaskAdmin(admin.ModelAdmin):
    list_display = ('id','c_type','s_id','t_name','c_name','condition','time_option','r_time','o_user_email','p_user_email','c_time','u_time')
    list_filter = ('c_type','o_user_email','p_user_email')
    search_fields = ('s_id','t_name','c_name','o_user_email','p_user_email')

admin.site.register(Error_task, ErrortaskAdmin)