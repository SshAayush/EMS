# Generated by Django 4.0.3 on 2022-11-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_staff_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='s_endtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='s_starttime',
            field=models.DateTimeField(),
        ),
    ]
