# Generated by Django 3.2.5 on 2021-08-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_onyx', models.CharField(max_length=3, verbose_name='ID на Onyx-realty')),
                ('contact', models.CharField(max_length=255, verbose_name='Ссылка на скачивание контакта')),
                ('qr', models.CharField(max_length=25, verbose_name='QR code')),
                ('photo', models.ImageField(upload_to='main/static/images/user', verbose_name='Фото сотрудника')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('job', models.CharField(max_length=255, verbose_name='Должность')),
                ('text', models.TextField(verbose_name='Текст')),
                ('b1_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 1')),
                ('b1_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b1_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b1_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b1_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b1_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b1_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b2_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 2')),
                ('b2_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b2_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b2_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b2_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b2_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b2_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b3_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 3')),
                ('b3_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b3_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b3_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b3_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b3_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b3_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b4_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 4')),
                ('b4_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b4_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b4_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b4_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b4_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b4_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b5_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 5')),
                ('b5_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b5_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b5_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b5_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b5_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b5_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b6_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 6')),
                ('b6_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b6_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b6_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b6_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b6_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b6_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b7_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 7')),
                ('b7_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b7_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b7_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b7_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b7_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b7_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b8_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 8')),
                ('b8_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b8_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b8_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b8_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b8_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b8_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b9_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 9')),
                ('b9_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b9_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b9_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b9_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b9_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b9_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b10_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 10')),
                ('b10_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b10_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b10_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b10_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b10_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b10_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b11_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 11')),
                ('b11_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b11_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b11_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b11_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b11_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b11_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b12_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 12')),
                ('b12_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b12_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b12_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b12_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b12_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b12_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b13_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 13')),
                ('b13_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b13_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b13_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b13_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b13_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b13_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b14_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 14')),
                ('b14_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b14_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b14_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b14_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b14_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b14_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
                ('b15_power', models.CharField(choices=[('display: none;', 'Выключить'), ('display: flex;', 'Включить')], default='display: none;', max_length=255, verbose_name='Включение кнопки 15')),
                ('b15_color', models.CharField(choices=[('background-color: rgba(0, 67, 78, 1);', 'Темно-Зеленый'), ('background-color: rgba(18, 180, 30, 1);', 'Светло-Зеленый'), ('background-color: rgba(0, 136, 204, 1);', 'Голубой'), ('background-color: rgba(121, 59, 170, 1);', 'Фиолетовый'), ('background-color: rgba(255, 55, 52, 1);', 'Оранжевый'), ('background-color: rgba(255, 0, 92, 1);', 'Розовый'), ('background-color: rgba(0, 45, 109, 1)', 'Синий'), ('background-color: rgba(238, 130, 8, 1);', 'Светло-Оранжевый'), ('background-color: rgba(255, 0, 0, 1);', 'Красный'), ('background-color: rgba(35, 31, 32, 1);', 'Черный')], default='background-color: rgba(0, 67, 78, 1);', max_length=255, verbose_name='Цвет кнопки')),
                ('b15_icons', models.CharField(choices=[('phone', 'Телефон'), ('whatsapp', 'Whatsapp'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('email', 'Email'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('vk', 'Vk'), ('ok', 'Однокласники'), ('tiktok', 'Tiktok'), ('twitter', 'Twitter'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('link', 'Ссылка')], default='tel', max_length=255, verbose_name='Иконка')),
                ('b15_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('b15_b_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('b15_api_cho', models.CharField(choices=[('tel:+7', 'Телефон'), ('https://api.whatsapp.com/send?phone=7', 'Whatsapp'), ('https://t.me/', 'Telegram'), ('viber://mobile?number=+7', 'Viber'), ('mailto:', 'Email'), ('https://www.instagram.com/', 'Instagram'), ('https://www.facebook.com/', 'Facebook'), ('https://vk.com/', 'Vk'), ('https://ok.ru/', 'Однокласники'), ('https://www.tiktok.com/', 'Tiktok'), ('https://twitter.com/', 'Twitter'), ('https://www.youtube.com/channel/', 'Youtube'), ('https://ru.linkedin.com', 'Linkedin'), ('https://', 'Ссылка')], default='tel:+7', max_length=355, verbose_name='Функционал кнопки')),
                ('b15_api_inp', models.CharField(default='8 800 200 06 07', max_length=255, verbose_name='Ваши данные')),
            ],
            options={
                'verbose_name': 'страничку пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
