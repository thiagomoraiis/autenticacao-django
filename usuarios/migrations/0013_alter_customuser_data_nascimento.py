# Generated by Django 4.2 on 2023-04-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_alter_customuser_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
