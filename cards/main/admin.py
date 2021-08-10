from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class CategoryUser(admin.ModelAdmin):
    list_display = ("id", "my_id", "id_onyx", "name", "email")
    list_display_links = ("name",)
    save_on_top = True
    fieldsets = (
        (None, {
            "fields": (("my_id", "id_onyx", "qr_code", "contact"), )
        }),
        (None, {
            "fields": (("name", "job", "email", "phone", "text", "photo"),)
        }),
        ("Кнопка 1", {
            "classes": ("collapse",),
            "fields": (("b1_power", "b1_color", "b1_icons", "b1_api_cho", "b1_title", "b1_b_text", "b1_api_inp"),)
        }),
        ("Кнопка 2", {
            "classes": ("collapse",),
            "fields": (("b2_power", "b2_color", "b2_icons", "b2_api_cho", "b2_title", "b2_b_text", "b2_api_inp"),)
        }),
        ("Кнопка 3", {
            "classes": ("collapse",),
            "fields": (("b3_power", "b3_color", "b3_icons", "b3_api_cho", "b3_title", "b3_b_text", "b3_api_inp"),)
        }),
        ("Кнопка 4", {
            "classes": ("collapse",),
            "fields": (("b4_power", "b4_color", "b4_icons", "b4_api_cho", "b4_title", "b4_b_text", "b4_api_inp"),)
        }),
        ("Кнопка 5", {
            "classes": ("collapse",),
            "fields": (("b5_power", "b5_color", "b5_icons", "b5_api_cho", "b5_title", "b5_b_text", "b5_api_inp"),)
        }),
        ("Кнопка 6", {
            "classes": ("collapse",),
            "fields": (("b6_power", "b6_color", "b6_icons", "b6_api_cho", "b6_title", "b6_b_text", "b6_api_inp"),)
        }),
        ("Кнопка 7", {
            "classes": ("collapse",),
            "fields": (("b7_power", "b7_color", "b7_icons", "b7_api_cho", "b7_title", "b7_b_text", "b7_api_inp"),)
        }),
        ("Кнопка 8", {
            "classes": ("collapse",),
            "fields": (("b8_power", "b8_color", "b8_icons", "b8_api_cho", "b8_title", "b8_b_text", "b8_api_inp"),)
        }),
        ("Кнопка 9", {
            "classes": ("collapse",),
            "fields": (("b9_power", "b9_color", "b9_icons", "b9_api_cho", "b9_title", "b9_b_text", "b9_api_inp"),)
        }),
        ("Кнопка 10", {
            "classes": ("collapse",),
            "fields": (("b10_power", "b10_color", "b10_icons", "b10_api_cho", "b10_title", "b10_b_text", "b10_api_inp"),)
        }),
        ("Кнопка 11", {
            "classes": ("collapse",),
            "fields": (("b11_power", "b11_color", "b11_icons", "b11_api_cho", "b11_title", "b11_b_text", "b11_api_inp"),)
        }),
        ("Кнопка 12", {
            "classes": ("collapse",),
            "fields": (("b12_power", "b12_color", "b12_icons", "b12_api_cho", "b12_title", "b12_b_text", "b12_api_inp"),)
        }),
        ("Кнопка 13", {
            "classes": ("collapse",),
            "fields": (("b13_power", "b13_color", "b13_icons", "b13_api_cho", "b13_title", "b13_b_text", "b13_api_inp"),)
        }),
        ("Кнопка 14", {
            "classes": ("collapse",),
            "fields": (("b14_power", "b14_color", "b14_icons", "b14_api_cho", "b14_title", "b14_b_text", "b14_api_inp"),)
        }),
        ("Кнопка 15", {
            "classes": ("collapse",),
            "fields": (("b15_power", "b15_color", "b15_icons", "b15_api_cho", "b15_title", "b15_b_text", "b15_api_inp"),)
        }),

    )
