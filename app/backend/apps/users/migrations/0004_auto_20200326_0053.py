# Generated by Django 2.2 on 2020-03-26 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userpetti_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpetti',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.Imagen'),
        ),
    ]
