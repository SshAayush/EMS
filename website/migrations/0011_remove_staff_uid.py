# Generated by Django 4.0.3 on 2022-11-16 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_staff_uid_userslist_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='uid',
        ),
    ]
