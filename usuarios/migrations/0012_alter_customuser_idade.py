# Generated by Django 4.2 on 2023-04-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_alter_customuser_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
