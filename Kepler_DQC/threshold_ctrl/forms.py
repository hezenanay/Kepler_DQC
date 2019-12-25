from django import forms
from .models import Threshold_task

class ThresholdtaskForm(forms.ModelForm):

    class Meta:
        model=Threshold_task
        fields=(
            'c_type','t_name','c_name','condition','time_option','up_value',
            'down_value','r_time','o_user_email','p_user_email'
        )