# Generated by Django 3.0.8 on 2021-10-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_adocao', '0004_auto_20211008_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachorro',
            name='foto1',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]