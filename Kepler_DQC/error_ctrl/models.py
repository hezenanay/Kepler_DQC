from django.db import models

# Create your models here.

class Error_task(models.Model):

    error_ctrl_kv=(
        ('equal_zero','为0'),
        ('equal_null','为空'),
        ('equal_neg','为负'),
        ('delay','数据延迟'),
    )

    c_type=models.CharField(max_length=32, choices=error_ctrl_kv)
    s_id=models.CharField(max_length=32)
    t_name=models.CharField(max_length=128)
    c_name=models.CharField(max_length=128)
    r_time=models.TimeField()
    o_user_email=models.EmailField(max_length=128)
    p_user_email=models.EmailField(max_length=128)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.o_user_email

    class Meta:
        ordering=['-c_time']
        verbose_name='异常监控'
        verbose_name_plural='异常监控'