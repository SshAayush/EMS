# Generated by Django 4.0.3 on 2022-10-17 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_userslist_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='s_endtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='s_starttime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
