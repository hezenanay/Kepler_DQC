from django import forms
from .models import Error_task

class ErrorctrlForm(forms.ModelForm):
    def clean_s_id(self):
        cleaned_data=self.cleaned_data['s_id']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')

    class Meta:
        model = Error_task
        fields=(
            's_id','t_name','c_name','condition','time_option',
            'r_time','o_user_email','p_user_email'
        )