# Generated by Django 4.1.5 on 2023-06-26 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastFood', '0003_remove_user_name_remove_user_surname_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
