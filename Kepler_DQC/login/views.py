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
        print(login_form)
        print(login_form.is_valid())
        if login_form.is_valid():
            print('提交数据有效')
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
    print('提交数据无效')
    login_form = UserFrom()
    return render(request, 'login/login.html', locals())

def logout(request):
    print('调用登出')
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        print('本来就未登录')
        return redirect("/login/")
    request.session.flush()
    print('session已清空')
    # flush会一次性清空session中所有内容，可以使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")