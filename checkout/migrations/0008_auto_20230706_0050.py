# Generated by Django 3.2.19 on 2023-07-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_show_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='show_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
