# Generated by Django 3.2.19 on 2023-07-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=10)),
            ],
        ),
    ]
