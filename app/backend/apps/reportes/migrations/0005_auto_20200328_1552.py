# Generated by Django 2.2.10 on 2020-03-28 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200327_0617'),
        ('reportes', '0004_auto_20200328_1524'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoReporte',
        ),
        migrations.AddField(
            model_name='reportenecesidad',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.UsuarioCovid'),
            preserve_default=False,
        ),
    ]
