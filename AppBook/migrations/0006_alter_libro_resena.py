# Generated by Django 5.0.6 on 2024-06-07 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBook', '0005_alter_libro_resena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='resena',
            field=models.TextField(default='Sin reseñas'),
        ),
    ]
