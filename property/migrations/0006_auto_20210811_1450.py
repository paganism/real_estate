# Generated by Django 2.2.4 on 2021-08-11 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='who_liked',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complained_flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complained_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
