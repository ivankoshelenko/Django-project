# Generated by Django 4.1.5 on 2023-01-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0003_rename_allimg_statsimages_allimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statsimages',
            name='allImg',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='statsimages',
            name='fullStackImg',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
