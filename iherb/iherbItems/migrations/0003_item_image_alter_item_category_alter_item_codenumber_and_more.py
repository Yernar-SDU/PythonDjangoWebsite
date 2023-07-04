# Generated by Django 4.1.5 on 2023-04-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iherbItems', '0002_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='iherbItems/img/banner/banner-1.jpg', upload_to='img/', verbose_name='My Photo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='Bestseller', help_text='Trend, Bestseller or something', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='codeNumber',
            field=models.CharField(default=3245425324, help_text='The code of the product', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='asdff', max_length=100000),
        ),
        migrations.AlterField(
            model_name='item',
            name='factory',
            field=models.CharField(default='ChildLife', help_text='Builed factory name', max_length=70),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=20, help_text='The count inside one package'),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(default=12, help_text='The size of item in inches', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='upcNumber',
            field=models.CharField(default='32454654234', help_text='The UPC number of the product', max_length=100),
        ),
    ]