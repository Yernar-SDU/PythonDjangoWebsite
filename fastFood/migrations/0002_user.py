# Generated by Django 4.1.5 on 2023-06-26 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastFood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]