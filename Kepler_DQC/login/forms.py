from django import forms

class UserFrom(forms.Form):
    username=forms.CharField(label='用户名', max_length=128, widget=forms.TextInput())
    password=forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput())