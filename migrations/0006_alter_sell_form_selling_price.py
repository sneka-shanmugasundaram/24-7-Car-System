# Generated by Django 5.0.5 on 2024-05-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_sell_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_form',
            name='selling_price',
            field=models.CharField(max_length=100, null=True),
        ),
    ]