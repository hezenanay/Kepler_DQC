from django import forms
from .models import User

# class UserFrom(forms.ModelForm):
#
#     class Meta:
#         model=User
#         fields=(
#             'username','password'
#         )
#         widgets={
#             'username':forms.TextInput,
#             'password':forms.PasswordInput,
#         }


class UserFrom(forms.Form):
    username=forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class':'login_box'}))
    password=forms.CharField(label='密码', max_length=255, widget=forms.PasswordInput(attrs={'class':'login_box'}))

