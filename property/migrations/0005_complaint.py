# Generated by Django 2.2.4 on 2021-08-11 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20210811_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compliat_text', models.TextField(verbose_name='Текст жалобы')),
                ('complained_flat', models.ForeignKey(help_text='Квартира, на которую пожаловались', on_delete=django.db.models.deletion.CASCADE, to='property.Flat')),
                ('complained_user', models.ForeignKey(help_text='Кто жаловался', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
