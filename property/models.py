from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):

    created_at = models.DateTimeField(
        "Когда создано объявление",
        default=timezone.now, db_index=True
        )

    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField(
        "Город, где находится квартира",
        max_length=50,
        db_index=True
        )
    town_district = models.CharField(
        "Район города, где находится квартира",
        max_length=50,
        blank=True,
        help_text='Чертаново Южное'
        )
    address = models.TextField(
        "Адрес квартиры",
        help_text='ул. Подольских курсантов д.5 кв.4'
        )
    floor = models.CharField(
        "Этаж",
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
        )

    rooms_number = models.IntegerField(
        "Количество комнат в квартире", db_index=True
        )
    living_area = models.IntegerField(
        "количество жилых кв.метров",
        null=True,
        blank=True,
        db_index=True
        )

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField(
        "Год постройки здания",
        null=True,
        blank=True, db_index=True
        )
    new_building = models.NullBooleanField(db_index=True)

    who_liked = models.ManyToManyField(
        User,
        verbose_name="Кто лайкнул",
        blank=True,
        null=True,
        related_name='users_likes'
        )

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Complaint(models.Model):
    complained_user = models.ForeignKey(
        User, null=True,
        on_delete=models.SET_NULL,
        verbose_name="Кто жаловался",
        related_name='users_complains'
        )
    complained_flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name="Квартира, на которую пожаловались",
        related_name='flats_complains'
        )
    compliat_text = models.TextField("Текст жалобы")

    def __str__(self):
        return f"{self.complained_user} \
            {self.complained_flat} {self.compliat_text[:50]}"


class Owner(models.Model):
    owner = models.CharField("ФИО владельца", max_length=200)
    owners_phonenumber = models.CharField(
        max_length=20,
        verbose_name="Номер владельца"
        )
    owner_pure_phone = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name="Нормализованный номер владельца"
        )
    flats = models.ManyToManyField(
        Flat,
        related_name="flats_owners",
        verbose_name="Квартиры в собственности",
        db_index=True,
        blank=True,
        null=True
        )
