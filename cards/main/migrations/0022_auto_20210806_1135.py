# Generated by Django 3.2.5 on 2021-08-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210806_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='b10_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b11_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b12_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b13_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b14_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b15_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b1_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b2_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b3_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b4_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b5_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b6_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b7_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b8_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='b9_color',
            field=models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 55, 52, 1);', 'Розовый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки'),
        ),
    ]
