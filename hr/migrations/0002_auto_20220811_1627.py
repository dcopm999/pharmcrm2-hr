# Generated by Django 3.2.8 on 2022-08-11 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='date_birth',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='User'),
            preserve_default=False,
        ),
    ]