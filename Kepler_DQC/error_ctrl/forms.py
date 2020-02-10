from django import forms
from .models import Error_task

# class ErrorctrlForm(forms.ModelForm):
#     def clean_s_id(self):
#         cleaned_data=self.cleaned_data['s_id']
#         if not cleaned_data.isdigit():
#             raise forms.ValidationError('必须是数字！')
#
#     class Meta:
#         model = Error_task
#         fields=(
#             's_id','server_add','t_name','c_name','condition','time_option',
#             'r_time','o_user_email','p_user_email'
#         )

class ErrorctrlForm(forms.Form):
    c_type=forms.ChoiceField(label='监控类型', choices=Error_task.error_ctrl_kv)
    s_id=forms.CharField(label='调度id', max_length=32, required=False)
    server_add=forms.ChoiceField(label='数据服务器', required=False, choices=Error_task.server_add_kv)
    t_name=forms.CharField(label='监控表名称', max_length=128, required=False)
    c_name=forms.CharField(label='监控字段名称', max_length=128, required=False)
    condition=forms.CharField(label='监控条件', max_length=256, required=False)
    time_option=forms.ChoiceField(label='条件时间选择', required=False, choices=Error_task.time_option_kv)
    r_time=forms.TimeField(label='执行时间')
    p_user_email=forms.EmailField(label='推送人邮箱', max_length=128)