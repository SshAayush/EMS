# Generated by Django 4.0.3 on 2022-11-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_staff_s_endtime_alter_staff_s_starttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clockin', models.DateTimeField()),
                ('clockout', models.DateTimeField()),
            ],
        ),
    ]