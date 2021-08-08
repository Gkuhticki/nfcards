from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile, File
# Create your models here.
class User(models.Model):
    POWER = [
        ("display: none;", "Выключить"),
        ("display: flex;", "Включить")
    ]
    COLOR = [
        ("background-color: rgba(0, 67, 78, 1);", "Темно-Зеленый"),
        ("background-color: rgba(18, 180, 30, 1);", "Светло-Зеленый"),
        ("background-color: rgba(0, 136, 204, 1);", "Голубой"),
        ("background-color: rgba(121, 59, 170, 1);", "Фиолетовый"),
        ("background-color: rgba(255, 55, 52, 1);", "Оранжевый"),
        ("background-color: rgba(255, 0, 92, 1);", "Розовый"),
        ("background-color: rgba(0, 45, 109, 1)", "Синий"),
        ("background-color: rgba(238, 130, 8, 1);", "Светло-Оранжевый"),
        ("background-color: rgba(255, 0, 0, 1);", "Красный"),
        ("background-color: rgba(35, 31, 32, 1);", "Черный")
        ]
    ICONS = [
        ("phone", "Телефон"),
        ("whatsapp", "Whatsapp"),
        ("telegram", "Telegram"),
        ("viber", "Viber"),
        ("email", "Email"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("vk", "Vk"),
        ("ok", "Однокласники"),
        ("tiktok", "Tiktok"),
        ("twitter", "Twitter"),
        ("youtube", "Youtube"),
        ("linkedin", "Linkedin"),
        ("link", "Ссылка")
    ]
    API_CHO = [
        ("tel:+7", "Телефон"),
        ("https://api.whatsapp.com/send?phone=7", "Whatsapp"),
        ("https://t.me/", "Telegram"),
        ("viber://mobile?number=+7", "Viber"),
        ("mailto:", "Email"),
        ("https://www.instagram.com/", "Instagram"),
        ("https://www.facebook.com/", "Facebook"),
        ("https://vk.com/", "Vk"),
        ("https://ok.ru/", "Однокласники"),
        ("https://www.tiktok.com/", "Tiktok"),
        ("https://twitter.com/", "Twitter"),
        ("https://www.youtube.com/channel/", "Youtube"),
        ("https://ru.linkedin.com", "Linkedin"),
        ("https://", "Ссылка")
    ]
    id_onyx = models.CharField(max_length=3, verbose_name="ID на Onyx-realty")
    contact = models.CharField(max_length=255, verbose_name="Ссылка на скачивание контакта")
    qr_code = models.ImageField(upload_to="main/static/images/griming/", blank=True)
    photo = models.ImageField(verbose_name="Фото сотрудника", upload_to="main/static/images/user")

    name = models.CharField(max_length=50, verbose_name="Имя")
    job = models.CharField(max_length=255, verbose_name="Должность")
    text = models.TextField(verbose_name="Текст")
    file = models.FileField(blank=True)



    b1_power = models.CharField(("Включение кнопки 1"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b1_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b1_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b1_title = models.CharField(("Заголовок"), max_length=255, )
    b1_b_text = models.CharField(("Текст"), max_length=255, )
    b1_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b1_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="страничку пользователя"
        verbose_name_plural = "Пользователи"


    def save(self, *args, **kwargs):
        # id = self.id
        # strid = str(id)
        #
        # url = "http://127.0.0.1:8000/user/"
        # furl = url + strid
        # qrcode_img = qrcode.make(furl)
        # canvas = Image.new('RGB', (390, 390), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code-{self.id}.png'
        # buffer = BytesIO()
        # canvas.save(buffer, 'PNG')
        # self.qr_code.save(fname, File(buffer), save=False)
        # canvas.close()

        myfile = ContentFile("hello world")
        new_name = "new_name.txt"
        self.file.save(new_name, File(myfile), save=False)

        super().save(*args, **kwargs)
