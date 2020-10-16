# Generated by Django 3.1.1 on 2020-10-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsManApp', '0003_auto_20201016_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='accountsManApp.Tag'),
        ),
    ]
