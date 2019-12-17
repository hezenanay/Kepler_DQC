from django.db import models

# Create your models here.

class User(models.Model):

    gender_kv=(
        ('male','男'),
        ('female','女'),
    )

    username=models.CharField(max_length=128, unique=True)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=128, unique=True)
    gender=models.CharField(max_length=32, choices=gender_kv, default='男')
    phone=models.CharField(max_length=32, unique=True)
    c_time=models.DateTimeField(auto_now_add=True)
    u_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering=['-c_time']
        verbose_name='用户'
        verbose_name_plural='用户'