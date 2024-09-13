# Generated by Django 5.0.3 on 2024-05-05 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunanibackapp', '0010_fotocooperativa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotocooperativa',
            name='cooperativa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='foto', to='tunanibackapp.cooperativa'),
        ),
    ]
