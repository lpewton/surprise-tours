# Generated by Django 3.2.19 on 2023-07-30 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_auto_20230730_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
    ]