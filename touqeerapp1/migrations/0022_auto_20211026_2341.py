# Generated by Django 3.1.4 on 2021-10-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0021_auto_20211026_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleproduct',
            name='name',
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='name',
            field=models.ManyToManyField(related_name='productName', to='touqeerapp1.Product'),
        ),
    ]