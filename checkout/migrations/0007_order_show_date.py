# Generated by Django 3.2.19 on 2023-07-02 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='show_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
