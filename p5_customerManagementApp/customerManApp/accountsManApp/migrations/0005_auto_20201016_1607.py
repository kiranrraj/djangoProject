# Generated by Django 3.1.1 on 2020-10-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsManApp', '0004_auto_20201016_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accountsManApp.Tag'),
        ),
    ]
