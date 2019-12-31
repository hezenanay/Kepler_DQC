from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *


# Create your views here.

def login(request):
    if request.session.get('is_login', None):
        #发现已登录则强制跳转到主页面
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserFrom(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    return redirect('/index/')
                else:
                    message = '密码不正确！'
            except:
                message = '用户不存在！'
        return render(request, 'login/login.html', locals())
    login_form = UserFrom()
    return render(request, 'login/login.html', locals())
