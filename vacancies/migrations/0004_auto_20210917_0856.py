# Generated by Django 3.2.7 on 2021-09-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_auto_20210917_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to='company_images'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to='speciality_images'),
        ),
    ]