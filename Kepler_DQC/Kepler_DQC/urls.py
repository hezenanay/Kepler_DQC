"""Kepler_DQC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from login import views as loginView
from dashboard import views as dashboardView
from error_ctrl import views as errorView
from threshold_ctrl import views as thresholdView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', loginView.login),
    url(r'^index/', dashboardView.index),
    url(r'^threshold_ctrl/', thresholdView.threshold_ctrl),
    url(r'^error_ctrl/', errorView.error_ctrl),
    url(r'^new_error_ctrl/', errorView.new_error_ctrl),
    url(r'^new_threshold_ctrl/', thresholdView.new_threshold_ctrl),
    url(r'^threshold_ctrl_dtl/(?P<post_id>\d+)/$', thresholdView.threshold_ctrl_dtl),
    url(r'^error_ctrl_dtl/(?P<post_id>\d+)/$', errorView.error_ctrl_dtl),
    url(r'^$', loginView.login),
    url(r'^logout/', loginView.logout),

]
