from django.db import models

# Create your models here.

class Threshold_task(models.Model):

    threshold_ctrl_kv=(
        ('value','上下限值'),
        ('percent','上下限百分比'),
    )

    c_type=models.CharField(verbose_name='监控类型', max_length=32, choices=threshold_ctrl_kv)
    t_name=models.CharField(verbose_name='监控表名称', max_length=128)
    c_name=models.CharField(verbose_name='监控字段名称', max_length=128)
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