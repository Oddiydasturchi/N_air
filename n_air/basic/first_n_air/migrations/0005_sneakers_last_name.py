# Generated by Django 4.0.4 on 2023-04-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_n_air', '0004_advertising'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='last_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
