# Generated by Django 2.2.7 on 2020-05-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='邮箱')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32, verbose_name='性别')),
                ('phone', models.CharField(max_length=32, unique=True, verbose_name='电话')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('u_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户',
                'ordering': ['-c_time'],
                'verbose_name_plural': '用户',
            },
        ),
    ]
