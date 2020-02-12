from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *


# Create your views here.

# 阈值监控页面
def threshold_ctrl(request):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    # 获取登录用户邮箱，获取用户任务列表
    user_email=request.session.get('user_email',None)
    task_list=Threshold_task.objects.filter(o_user_email=user_email)

    # 新建监控按钮
    if request.method == 'POST':
        # 如果请求来自新建监控按钮
        if 'new_ctrl' in request.POST:
            return redirect('/new_threshold_ctrl/')

    # 生成当前用户下的任务内容
    context = {
        'task_list': task_list
    }

    return render(request, 'threshold_ctrl/threshold_ctrl.html', locals())



# 新建阈值监控页面
def new_threshold_ctrl(request):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    if request.method == 'POST':
        threshold_form = ThresholdtaskForm(request.POST)
        if threshold_form.is_valid():
            cleaned_data = threshold_form.cleaned_data
            c_type = cleaned_data['c_type']
            server_add = cleaned_data['server_add']
            t_name = cleaned_data['t_name']
            c_name = cleaned_data['c_name']
            condition = cleaned_data['condition']
            time_option = cleaned_data['time_option']
            cpr_time_option = cleaned_data['cpr_time_option']
            up_value = cleaned_data['up_value']
            down_value = cleaned_data['down_value']
            r_time = cleaned_data['r_time']
            o_user_email = request.session.get('user_email')
            p_user_email = cleaned_data['p_user_email']
            if c_type == None or r_time == None or server_add == None or t_name == None or c_name == None or up_value == None or down_value == None or o_user_email == None or p_user_email == None:
                message = '请检查必填项是否完整！'
                return render(request, 'threshold_ctrl/new_threshold_ctrl.html', locals())
            if c_type == 'percent' and (condition == None or time_option == None or cpr_time_option == None):
                message = '请检查必填项是否完整！'
                return render(request, 'threshold_ctrl/new_threshold_ctrl.html', locals())

            # 当一切ok的情况下，创建新任务

            new_task = Threshold_task()
            new_task.c_type = c_type
            new_task.server_add = server_add
            new_task.t_name = t_name
            new_task.c_name = c_name
            new_task.condition = condition
            new_task.time_option = time_option
            new_task.cpr_time_option = cpr_time_option
            new_task.up_value = up_value
            new_task.down_value = down_value
            new_task.r_time = r_time
            new_task.o_user_email = o_user_email
            new_task.p_user_email = p_user_email
            new_task.save()
            return redirect('/threshold_ctrl/')
    threshold_form = ThresholdtaskForm()
    return render(request, 'threshold_ctrl/new_threshold_ctrl.html', locals())



# 阈值监控编辑界面
def threshold_ctrl_dtl(request, post_id):
    if not request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    task_detail=Threshold_task.objects.get(id=post_id)

    # 生成当前任务的详细信息
    context = {
        'task_detail': task_detail
    }


    # 删除按钮
    if request.method == 'POST':
        # 如果请求来自删除按钮
        if 'delete' in request.POST:
            Threshold_task.objects.filter(id=post_id).delete()
            return redirect('/threshold_ctrl/')

    # 修改按钮
    if request.method == 'POST':
        # 如果请求来自修改按钮
        if 'update' in request.POST:
            # 更新内容占位
            # Threshold_task.objects.filter(id=post_id).update(#更新内容占位)
            return redirect('/threshold_ctrl/')

    return render(request, 'threshold_ctrl/threshold_ctrl_dtl.html', locals())