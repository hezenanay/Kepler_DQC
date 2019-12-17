from django.db import models

# Create your models here.

class Threshold_task(models.Model):

    threshold_ctrl_kv=(
        ('value','上下限值'),
        ('percent','上下限百分比'),
    )

    c_type=models.CharField(max_length=32, choices=threshold_ctrl_kv)
    t_name=models.CharField(max_length=128)
    c_name=models.CharField(max_length=128)
    up_value=models.DecimalField(max_digits=16, decimal_places=2)
    down_value=models.DecimalField(max_digits=16, decimal_places=2)
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