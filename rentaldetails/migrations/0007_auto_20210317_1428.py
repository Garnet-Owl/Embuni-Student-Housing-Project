# Generated by Django 3.1.6 on 2021-03-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentaldetails', '0006_auto_20210302_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Image_url',
        ),
        migrations.AddField(
            model_name='detail',
            name='Image_url1',
            field=models.CharField(default=0, max_length=2090),
            preserve_default=False,
        ),
    ]