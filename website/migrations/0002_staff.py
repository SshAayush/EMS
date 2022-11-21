# Generated by Django 4.0.3 on 2022-10-17 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_fname', models.CharField(max_length=100)),
                ('s_lname', models.CharField(max_length=100)),
                ('s_Email', models.EmailField(max_length=50)),
                ('s_starttime', models.DateTimeField(auto_now=True)),
                ('s_endtime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
