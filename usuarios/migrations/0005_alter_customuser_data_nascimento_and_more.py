# Generated by Django 4.2 on 2023-04-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data_nascimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]