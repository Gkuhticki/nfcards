# Generated by Django 3.2.5 on 2021-08-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210805_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icons',
            field=models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка'),
        ),
    ]