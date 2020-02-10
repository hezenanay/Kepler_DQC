from django import forms
from .models import Threshold_task

# class ThresholdtaskForm(forms.ModelForm):
#
#     class Meta:
#         model=Threshold_task
#         fields=(
#             'c_type','server_add','t_name','c_name','condition','time_option','cpr_time_option','up_value',
#             'down_value','r_time','o_user_email','p_user_email'
#         )

class ThresholdtaskForm(forms.Form):
    c_type=forms.ChoiceField(label='监控类型', choices=Threshold_task.threshold_ctrl_kv)
    server_add=forms.ChoiceField(label='数据服务器', choices=Threshold_task.server_add_kv)
    t_name=forms.CharField(label='监控表名称', max_length=128)
    c_name=forms.CharField(label='监控字段名称', max_length=128)
    condition=forms.CharField(label='监控条件', max_length=256, required=False)
    time_option=forms.ChoiceField(label='监控条件时间选择', required=False, choices=Threshold_task.time_option_kv)
    cpr_time_option=forms.ChoiceField(label='对比条件时间选择', required=False, choices=Threshold_task.time_option_kv)
    up_value=forms.FloatField(label='监控上限')
    down_value=forms.FloatField(label='监控下限')
    r_time = forms.TimeField(label='执行时间')
    p_user_email = forms.EmailField(label='推送人邮箱', max_length=128)