# Generated by Django 3.2.9 on 2022-03-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
