from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile, File
import vobject


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
    # Поле my_id создаеться по причине того что пока не получилось вытащить поле id через self в функцию save ниже.
    # Поле id_onyx необходимо для создания ссылки на страницу пользователя на другом сайте
    # Поле contact берет данные с функции save ниже
    # Поле qr_code берет данные с функции save ниже
    my_id = models.CharField(max_length=5, verbose_name="ID Страницы на сайте")
    id_onyx = models.CharField(max_length=3, verbose_name="ID на Onyx-realty")
    contact = models.FileField(blank=True, verbose_name="Контакт VCF Заполняется автоматически")
    qr_code = models.ImageField(upload_to="main/static/images/griming/",
                                blank=True, verbose_name="qr code Заполняется автоматически")
    photo = models.ImageField(upload_to="main/static/images/user", verbose_name="Фото сотрудника")

    name = models.CharField(max_length=50, verbose_name="Имя")
    job = models.CharField(max_length=255, verbose_name="Должность")
    text = models.TextField(verbose_name="Описание")
    email = models.CharField(max_length=55, default="reception@onyx-realty.ru")
    phone = models.CharField("Телефон", max_length=25, default="89882360607")

    # Далее пошли кнопки
    # По умолчанию первая кнопка телефон
    b1_power = models.CharField("Включение кнопки 1", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b1_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(0, 67, 78, 1);")
    b1_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="phone")
    b1_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False, default="tel:+7")
    b1_title = models.CharField("Имя кнопки", max_length=255, default="Телефон")
    b1_b_text = models.CharField("Текст кнопки", max_length=255, default="8(988) 236 06 07")
    b1_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="9882360607")

    # По умолчанию вторая кнопка Whatsapp
    b2_power = models.CharField("Включение кнопки 2", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b2_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(18, 180, 30, 1);")
    b2_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="whatsapp")
    b2_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://api.whatsapp.com/send?phone=7")
    b2_title = models.CharField("Имя кнопки", max_length=255, default="Whatsapp")
    b2_b_text = models.CharField("Текст кнопки", max_length=255, default="8(988) 236 06 07")
    b2_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="9882360607")

    # По умолчанию третья кнопка Viber
    b3_power = models.CharField("Включение кнопки 3", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b3_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(121, 59, 170, 1);")
    b3_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="viber")
    b3_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="viber://mobile?number=+7")
    b3_title = models.CharField("Имя кнопки", max_length=255, default="Viber")
    b3_b_text = models.CharField("Текст кнопки", max_length=255, default="8(988) 236 06 07")
    b3_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="9882360607")

    # По умолчанию четвертая кнопка Telegram
    b4_power = models.CharField("Включение кнопки 4", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b4_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(0, 136, 204, 1);")
    b4_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="telegram")
    b4_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://t.me/")
    b4_title = models.CharField("Имя кнопки", max_length=255, default="Telegram")
    b4_b_text = models.CharField("Текст кнопки", max_length=255, default="@onyxrealtysochi")
    b4_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="@onyxrealtysochi")

    # По умолчанию пятая кнопка Email
    b5_power = models.CharField("Включение кнопки 5", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b5_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(255, 55, 52, 1);")
    b5_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="email")
    b5_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="mailto:")
    b5_title = models.CharField("Имя кнопки", max_length=255, default="Email")
    b5_b_text = models.CharField("Текст кнопки", max_length=255, default="reception@onyx-realty.ru")
    b5_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="reception@onyx-realty.ru")

    # По умолчанию шестая кнопка Instagram
    b6_power = models.CharField("Включение кнопки 6", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b6_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(255, 0, 92, 1);")
    b6_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="instagram")
    b6_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://www.instagram.com/")
    b6_title = models.CharField("Имя кнопки", max_length=255, default="Instagram")
    b6_b_text = models.CharField("Текст кнопки", max_length=255, default="@onyxrealty")
    b6_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyxrealty")

    # По умолчанию седьмая кнопка Tiktok
    b7_power = models.CharField("Включение кнопки 7", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b7_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(35, 31, 32, 1);")
    b7_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="tiktok")
    b7_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://www.tiktok.com/")
    b7_title = models.CharField("Имя кнопки", max_length=255, default="Tiktok")
    b7_b_text = models.CharField("Текст кнопки", max_length=255, default="@onyxrealty")
    b7_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="@onyxrealty")

    # По умолчанию восьмая кнопка Facebook
    b8_power = models.CharField("Включение кнопки 8", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b8_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(0, 45, 109, 1)")
    b8_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="facebook")
    b8_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://www.facebook.com/")
    b8_title = models.CharField("Имя кнопки", max_length=255, default="Facebook")
    b8_b_text = models.CharField("Текст кнопки", max_length=255, default="onyxsochi")
    b8_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyxsochi")

    # По умолчанию девятая кнопка Vk
    b9_power = models.CharField("Включение кнопки 9", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b9_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(0, 45, 109, 1)")
    b9_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="vk")
    b9_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://vk.com/")
    b9_title = models.CharField("Имя кнопки", max_length=255, default="Vk")
    b9_b_text = models.CharField("Текст кнопки", max_length=255, default="onyxrealty")
    b9_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyxrealty2012")

    # По умолчанию десятая кнопка OK
    b10_power = models.CharField("Включение кнопки 10", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b10_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(238, 130, 8, 1);")
    b10_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="ok")
    b10_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://ok.ru/")
    b10_title = models.CharField("Имя кнопки", max_length=255, default="Одноклассники")
    b10_b_text = models.CharField("Текст кнопки", max_length=255, default="onyxrealty")
    b10_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="profile/565444096834/")

    # По умолчанию одинадцатая кнопка Youtube
    b11_power = models.CharField("Включение кнопки 11", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b11_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(255, 0, 0, 1);")
    b11_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="youtube")
    b11_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://www.youtube.com/channel/")
    b11_title = models.CharField("Имя кнопки", max_length=255, default="Youtube")
    b11_b_text = models.CharField("Текст кнопки", max_length=255, default="Onyxrealty")
    b11_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="UC8hfz3LpB3g7oMoel_bJG5g")

    # По умолчанию двенадцатая кнопка Twitter
    b12_power = models.CharField("Включение кнопки 12", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b12_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(0, 136, 204, 1);")
    b12_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="twitter")
    b12_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://twitter.com/")
    b12_title = models.CharField("Имя кнопки", max_length=255, default="Twitter")
    b12_b_text = models.CharField("Текст кнопки", max_length=255, default="RealtyOnyx")
    b12_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="RealtyOnyx")

    # По умолчанию оставшиеся кнопки ссылки
    b13_power = models.CharField("Включение кнопки 13", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b13_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(35, 31, 32, 1);")
    b13_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="link")
    b13_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://")
    b13_title = models.CharField("Имя кнопки", max_length=255, default="link to")
    b13_b_text = models.CharField("Текст кнопки", max_length=255, default="Onyx Realty")
    b13_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyx-realty.ru/")

    b14_power = models.CharField("Включение кнопки 14", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b14_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(35, 31, 32, 1);")
    b14_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="link")
    b14_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://")
    b14_title = models.CharField("Имя кнопки", max_length=255, default="link to")
    b14_b_text = models.CharField("Текст кнопки", max_length=255, default="Onyx Realty")
    b14_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyx-realty.ru/")

    b15_power = models.CharField("Включение кнопки 15", choices=POWER, max_length=255, blank=False,
                                default="display: none;")
    b15_color = models.CharField("Цвет кнопки", choices=COLOR, max_length=255, blank=False,
                                default="background-color: rgba(35, 31, 32, 1);")
    b15_icons = models.CharField("Иконка", choices=ICONS, max_length=255, blank=False, default="link")
    b15_api_cho = models.CharField("Функционал кнопки", choices=API_CHO, max_length=355, blank=False,
                                  default="https://")
    b15_title = models.CharField("Имя кнопки", max_length=255, default="link to")
    b15_b_text = models.CharField("Текст кнопки", max_length=255, default="Onyx Realty")
    b15_api_inp = models.CharField(verbose_name="Ваши данные", max_length=255, default="onyx-realty.ru/")




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "страничку пользователя"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        # Передаем данные в qr_code.
        url = f"http://127.0.0.1:8000/user/{self.my_id}"
        qrcode_img = qrcode.make(url)
        canvas = Image.new('RGB', (390, 390), 'white')
        canvas.paste(qrcode_img)
        name_of_qrcode = f'qr_code-{self.my_id}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(name_of_qrcode, File(buffer), save=False)
        canvas.close()

        # Передаем данные в contact.
        template_for_contact = ContentFile(
            f"""\
BEGIN:VCARD
VERSION:3.0
FN:{self.name}
N:{self.name};;;
item1.EMAIL;TYPE=INTERNET:{self.email}
item1.X-ABLabel:
item2.TEL:{self.phone}
item2.X-ABLabel:Рабочие контакты
item3.ORG:Оникс-Недвижимость
item3.X-ABLabel:
item4.TITLE:{self.job}
item4.X-ABLabel:
CATEGORIES:myContacts
END:VCARD
"""
        )
        name_of_contact = "contacts.vcf"
        self.contact.save(name_of_contact, File(template_for_contact), save=False)

        super().save(*args, **kwargs)
