# Generated by Django 3.1.4 on 2021-10-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0002_company_product_purchaseitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchaseitem',
            name='size',
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='discountPercent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='gst',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='scheme',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]