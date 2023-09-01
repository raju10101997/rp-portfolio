# Generated by Django 3.2.13 on 2022-06-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descripton', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
