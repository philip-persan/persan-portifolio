# Generated by Django 4.0.4 on 2022-05-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_owner_freelance_alter_owner_open_to_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
    ]
