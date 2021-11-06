# Generated by Django 3.1.4 on 2021-10-25 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touqeerapp1', '0015_auto_20211025_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='sales',
        ),
        migrations.AddField(
            model_name='sale',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='touqeerapp1.orderitem'),
        ),
    ]