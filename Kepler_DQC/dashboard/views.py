from django.shortcuts import render
from django.shortcuts import redirect
import hashlib
from .forms import *
from .models import *
# Create your views here.

def index(request):
    if request.session.get('is_login', None):
        # 发现没有登录则强制跳转到登录页面
        return redirect('/login/')
    return render(request, 'dashboard/dashboard.html', locals())