# Generated by Django 5.1 on 2024-08-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='shortName',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
