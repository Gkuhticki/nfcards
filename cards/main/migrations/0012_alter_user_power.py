# Generated by Django 3.2.5 on 2021-08-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210805_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], max_length=255, verbose_name='power'),
        ),
    ]