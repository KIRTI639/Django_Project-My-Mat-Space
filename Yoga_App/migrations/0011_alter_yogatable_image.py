# Generated by Django 4.0.5 on 2023-05-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoga_App', '0010_yogatable_disease_code_alter_yogatable_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yogatable',
            name='image',
            field=models.FileField(upload_to='media/img'),
        ),
    ]
