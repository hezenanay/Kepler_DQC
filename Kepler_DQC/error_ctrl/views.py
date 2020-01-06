from django.shortcuts import render
from django.shortcuts import redirect
import hashlib
from .forms import *
from .models import *


# Create your views here.

# 异常监控页面
def error_ctrl(request):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    # 获取登录用户邮箱，获取用户任务列表
    user_email=request.session.get('user_email', None)
    task_list = Error_task.objects.get(o_user_email=user_email)

    if request.method == 'POST':
        # 如果请求来自新建监控按钮
        if 'new_ctrl' in request.POST:
            return redirect('/new_error_ctrl/')

    # 生成当前用户下的任务内容
    context={
        'task_list':task_list
    }
    return render(request, 'error_ctrl/error_ctrl.html', context=context)

# 新建异常监控
def new_error_ctrl(request):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    if request.method == 'POST':
        error_form = ErrorctrlForm(request.POST)
        if error_form.is_valid():
            cleaned_data = error_form.cleaned_data
            c_type = cleaned_data['c_type']
            s_id = cleaned_data['s_id']
            server_add = cleaned_data['server_add']
            t_name = cleaned_data['t_name']
            c_name = cleaned_data['c_name']
            condition = cleaned_data['condition']
            time_option = cleaned_data['time_option']
            r_time = cleaned_data['r_time']
            o_user_email = cleaned_data['o_user_email']
            p_user_email = cleaned_data['p_user_email']
            if c_type == None or r_time == None or o_user_email == None or p_user_email == None:
                message = '请检查必填项是否完整！'
                return render(request, 'error_ctrl/new_error_ctrl.html', locals())
            if c_type == 'delay' and s_id == None:
                message = '请检查必填项是否完整！'
                return render(request, 'error_ctrl/new_error_ctrl.html', locals())
            if c_type in ['equal_zero', 'equal_null', 'equal_neg'] and (
                    server_add == None or t_name == None or c_name == None):
                message = '请检查必填项是否完整！'
                return render(request, 'error_ctrl/new_error_ctrl.html', locals())

            # 当一切ok的情况下，创建新任务

            new_task = Error_task()
            new_task.c_type = c_type
            new_task.s_id = s_id
            new_task.server_add = server_add
            new_task.t_name = t_name
            new_task.c_name = c_name
            new_task.condition = condition
            new_task.time_option = time_option
            new_task.r_time = r_time
            new_task.o_user_email = o_user_email
            new_task.p_user_email = p_user_email
            new_task.save()
            return redirect('/error_ctrl_list/')  # 自动跳转到异常监控列表页面
    error_form = ErrorctrlForm()
    return render(request, 'error_ctrl/new_error_ctrl.html', locals())
