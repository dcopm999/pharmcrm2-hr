# Generated by Django 2.2 on 2021-09-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20210930_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='is_working',
        ),
    ]