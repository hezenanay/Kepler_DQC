# Generated by Django 2.2.7 on 2019-12-18 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threshold_ctrl', '0002_auto_20191217_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threshold_task',
            options={'ordering': ['-c_time'], 'verbose_name': '阈值监控', 'verbose_name_plural': '阈值监控'},
        ),
    ]
