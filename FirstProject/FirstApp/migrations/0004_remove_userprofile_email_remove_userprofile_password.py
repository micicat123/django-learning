# Generated by Django 4.1 on 2022-08-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_userprofile_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]