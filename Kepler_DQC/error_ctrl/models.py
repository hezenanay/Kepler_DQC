from django.db import models

# Create your models here.

class Error_task(models.Model):

    error_ctrl_kv=(
        ('equal_zero','为0'),
        ('equal_null','为空'),
        ('equal_neg','为负'),
        ('delay','数据延迟'),
    )

    c_type=models.CharField(verbose_name='监控类型', max_length=32, choices=error_ctrl_kv)
    s_id=models.CharField(verbose_name='调度id', max_length=32, null=True, blank=True)
    t_name=models.CharField(verbose_name='监控表名称', max_length=128, null=True, blank=True)
    c_name=models.CharField(verbose_name='监控字段名称', max_length=128, null=True, blank=True)
    r_time=models.TimeField(verbose_name='执行时间')
    o_user_email=models.EmailField(verbose_name='创建人邮箱', max_length=128)
    p_user_email=models.EmailField(verbose_name='推送人邮箱', max_length=128)
    c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    u_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.o_user_email

    class Meta:
        ordering=['-c_time']
        verbose_name='异常监控'
        verbose_name_plural='异常监控'