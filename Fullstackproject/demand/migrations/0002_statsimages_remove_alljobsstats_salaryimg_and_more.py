# Generated by Django 4.1.5 on 2023-01-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllImg', models.ImageField(null=True, upload_to='static/img/')),
                ('SullStackImg', models.ImageField(null=True, upload_to='static/img/')),
            ],
        ),
        migrations.RemoveField(
            model_name='alljobsstats',
            name='SalaryImg',
        ),
        migrations.RemoveField(
            model_name='fullstackstats',
            name='SalaryImg',
        ),
    ]