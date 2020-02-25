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
    user_email = request.session.get('user_email', None)
    task_list = Error_task.objects.filter(o_user_email=user_email)
    print(task_list)


    # 新建监控按钮
    if request.method == 'POST':
        # 如果请求来自新建监控按钮
        if 'new_ctrl' in request.POST:
            return redirect('/new_error_ctrl/')

    # 生成当前用户下的任务内容
    context = {
        'task_list': task_list
    }
    return render(request, 'error_ctrl/error_ctrl.html', context=context)
    # return render(request, 'error_ctrl/error_ctrl.html')


# 新建异常监控
def new_error_ctrl(request):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    if request.method == 'POST':
        error_form = ErrorctrlForm(request.POST)
        if error_form.is_valid():
            print('新建任务数据有效')
            cleaned_data = error_form.cleaned_data
            c_type = cleaned_data['c_type']
            s_id = cleaned_data['s_id']
            server_add = cleaned_data['server_add']
            t_name = cleaned_data['t_name']
            c_name = cleaned_data['c_name']
            condition = cleaned_data['condition']
            time_option = cleaned_data['time_option']
            r_time = cleaned_data['r_time']
            o_user_email = request.session.get('user_email')
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
            return redirect('/error_ctrl/')  # 自动跳转到异常监控列表页面
    error_form = ErrorctrlForm()
    return render(request, 'error_ctrl/new_error_ctrl.html', locals())


# 异常监控编辑界面
def error_ctrl_dtl(request, post_id):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    task_detail = Error_task.objects.filter(id=post_id, o_user_email=request.session.get('user_email'))


    # 生成当前任务的详细信息
    context = {
        'task_detail': task_detail
    }

    print(task_detail)
    # 删除按钮
    if request.method == 'POST':
        print('发生了请求')
        # 如果请求来自删除按钮
        if 'delete' in request.POST:
            print('已点击删除')
            Error_task.objects.filter(id=post_id).delete()
            return redirect('/error_ctrl/')

        # 修改按钮
        # 如果请求来自修改按钮
        elif 'update' in request.POST:
            new_c_type=request.POST.get('new_c_type')
            new_s_id=request.POST.get('new_s_id')
            new_server_add=request.POST.get('new_server_add')
            new_t_name=request.POST.get('new_t_name')
            new_c_name=request.POST.get('new_c_name')
            new_condition=request.POST.get('new_condition')
            new_time_option=request.POST.get('new_time_option')
            new_r_time=request.POST.get('new_r_time')
            new_p_user_email=request.POST.get('new_p_user_email')

            task=task_detail[0]
            task.c_type=new_c_type
            task.s_id=new_s_id
            task.server_add=new_server_add
            task.t_name=new_t_name
            task.c_name=new_c_name
            task.condition=new_condition
            task.time_option=new_time_option
            task.r_time=new_r_time
            task.p_user_email=new_p_user_email
            task.save()
            return redirect('/error_ctrl/')
    print('没有发现post')
    return render(request, 'error_ctrl/error_ctrl_dtl.html', context=context)
    # return render(request, 'error_ctrl/error_ctrl_dtl.html', locals())
