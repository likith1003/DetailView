# Generated by Django 5.0.4 on 2024-04-05 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.school'),
        ),
    ]
