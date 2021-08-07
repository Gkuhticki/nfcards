from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
from io import BytesIO
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




    b1_power = models.CharField(("Включение кнопки 1"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b1_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b1_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b1_title = models.CharField(("Заголовок"), max_length=255, )
    b1_b_text = models.CharField(("Текст"), max_length=255, )
    b1_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b1_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b2_power = models.CharField(("Включение кнопки 2"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b2_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b2_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b2_title = models.CharField(("Заголовок"), max_length=255, )
    b2_b_text = models.CharField(("Текст"), max_length=255, )
    b2_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b2_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b3_power = models.CharField(("Включение кнопки 3"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b3_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b3_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b3_title = models.CharField(("Заголовок"), max_length=255, )
    b3_b_text = models.CharField(("Текст"), max_length=255, )
    b3_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b3_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b4_power = models.CharField(("Включение кнопки 4"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b4_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b4_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b4_title = models.CharField(("Заголовок"), max_length=255, )
    b4_b_text = models.CharField(("Текст"), max_length=255, )
    b4_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b4_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b5_power = models.CharField(("Включение кнопки 5"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b5_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b5_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b5_title = models.CharField(("Заголовок"), max_length=255, )
    b5_b_text = models.CharField(("Текст"), max_length=255, )
    b5_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b5_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b6_power = models.CharField(("Включение кнопки 6"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b6_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b6_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b6_title = models.CharField(("Заголовок"), max_length=255, )
    b6_b_text = models.CharField(("Текст"), max_length=255, )
    b6_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b6_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b7_power = models.CharField(("Включение кнопки 7"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b7_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b7_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b7_title = models.CharField(("Заголовок"), max_length=255, )
    b7_b_text = models.CharField(("Текст"), max_length=255, )
    b7_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b7_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b8_power = models.CharField(("Включение кнопки 8"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b8_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b8_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b8_title = models.CharField(("Заголовок"), max_length=255, )
    b8_b_text = models.CharField(("Текст"), max_length=255, )
    b8_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b8_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b9_power = models.CharField(("Включение кнопки 9"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b9_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b9_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b9_title = models.CharField(("Заголовок"), max_length=255, )
    b9_b_text = models.CharField(("Текст"), max_length=255, )
    b9_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b9_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b10_power = models.CharField(("Включение кнопки 10"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b10_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b10_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b10_title = models.CharField(("Заголовок"), max_length=255, )
    b10_b_text = models.CharField(("Текст"), max_length=255, )
    b10_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b10_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b11_power = models.CharField(("Включение кнопки 11"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b11_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b11_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b11_title = models.CharField(("Заголовок"), max_length=255, )
    b11_b_text = models.CharField(("Текст"), max_length=255, )
    b11_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b11_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b12_power = models.CharField(("Включение кнопки 12"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b12_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b12_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b12_title = models.CharField(("Заголовок"), max_length=255, )
    b12_b_text = models.CharField(("Текст"), max_length=255, )
    b12_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b12_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b13_power = models.CharField(("Включение кнопки 13"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b13_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b13_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b13_title = models.CharField(("Заголовок"), max_length=255, )
    b13_b_text = models.CharField(("Текст"), max_length=255, )
    b13_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b13_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b14_power = models.CharField(("Включение кнопки 14"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b14_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b14_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b14_title = models.CharField(("Заголовок"), max_length=255, )
    b14_b_text = models.CharField(("Текст"), max_length=255, )
    b14_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b14_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    b15_power = models.CharField(("Включение кнопки 15"), choices=POWER, max_length=255, blank=False, default="display: none;")
    b15_color = models.CharField(("Цвет кнопки"), choices=COLOR, max_length=255, blank=False, default="background-color: rgba(0, 67, 78, 1);")
    b15_icons = models.CharField(("Иконка"), choices=ICONS, max_length=255, blank=False, default="tel")
    b15_title = models.CharField(("Заголовок"), max_length=255, )
    b15_b_text = models.CharField(("Текст"), max_length=255, )
    b15_api_cho = models.CharField(("Функционал кнопки"), choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b15_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="8 800 200 06 07")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="страничку пользователя"
        verbose_name_plural = "Пользователи"

    # def Test(self):
    #     id = self.id
    #     strid = str(id)
    #
    #     url = "http://127.0.0.1:8000/user/"
    #     furl = url + strid
    #     img = qrcode.make(furl)
    #     img.save('myqrcode.png')
    #
    #
    #     a = 500
    #     aa = str(a)
    #     cc = strid + aa
    #     id1 = cc
    #
    #     return id1

    def save(self, *args, **kwargs):
        id = self.id
        strid = str(id)

        url = "http://127.0.0.1:8000/user/"
        furl = url + strid
        qrcode_img = qrcode.make(furl)
        canvas = Image.new('RGB', (390, 390), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)