from django.db import models

# Create your models here.

class Threshold_task(models.Model):

    threshold_ctrl_kv=(
        ('value','上下限值'),
        ('percent','上下限百分比'),
    )

    time_option_kv=(
        ('today','今天(yyyy-mm-dd)'),
        ('yesterday','昨天(yyyy-mm-dd)'),
        ('now_year','当年(yyyy)'),
        ('now_month','当月(yyyy-mm)'),
        ('now_month_only','当月(mm)'),
        ('last_month','上月(yyyy-mm)'),
        ('last_month_only','上月(mm)'),
    )

    server_add_kv = (
        ('10.130.146.11', '报表平台 (10.130.146.11)'),
        ('10.130.146.13', '决策系统 (10.130.146.13)'),
        ('10.126.75.56', '虚拟机 (10.126.75.56)'),
    )

    c_type=models.CharField(verbose_name='监控类型', max_length=32, choices=threshold_ctrl_kv)
    server_add = models.CharField(verbose_name='数据服务器', max_length=128, null=True, blank=True, choices=server_add_kv)
    t_name=models.CharField(verbose_name='监控表名称', max_length=128)
    c_name=models.CharField(verbose_name='监控字段名称', max_length=128)
    condition = models.CharField(verbose_name='监控条件', max_length=256, null=True, blank=True)
    time_option = models.CharField(verbose_name='条件时间选择', max_length=128, null=True, blank=True, choices=time_option_kv)
    up_value=models.DecimalField(verbose_name='监控上限值、百分比', max_digits=16, decimal_places=2)
    down_value=models.DecimalField(verbose_name='监控下限值、百分比', max_digits=16, decimal_places=2)
    r_time=models.TimeField(verbose_name='执行时间')
    o_user_email=models.EmailField(verbose_name='创建人邮箱', max_length=128)
    p_user_email=models.EmailField(verbose_name='推送人邮箱', max_length=128)
    c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    u_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.o_user_email

    class Meta:
        ordering=['-c_time']
        verbose_name='阈值监控'
        verbose_name_plural='阈值监控'