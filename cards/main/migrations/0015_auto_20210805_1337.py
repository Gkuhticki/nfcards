# Generated by Django 3.2.5 on 2021-08-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210805_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='area_1_2',
        ),
        migrations.AddField(
            model_name='user',
            name='b_text',
            field=models.CharField(default=1, max_length=255, verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
