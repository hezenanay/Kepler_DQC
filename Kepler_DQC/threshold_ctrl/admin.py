from django.contrib import admin

# Register your models here.

from .models import Threshold_task

class ThresholdtaskAdmin(admin.ModelAdmin):
    list_display = ('id','c_type','t_name','c_name','condition','time_option','up_value','down_value','r_time','o_user_email','p_user_email','notes','t_state','c_state','c_time','u_time')
    list_filter = ('c_type','o_user_email','p_user_email','t_state','c_state')
    search_fields = ('t_name','c_name','o_user_email','p_user_email')

admin.site.register(Threshold_task, ThresholdtaskAdmin)