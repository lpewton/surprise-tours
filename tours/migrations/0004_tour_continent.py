# Generated by Django 3.2.19 on 2023-06-05 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20230605_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='continent',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tours.continent'),
            preserve_default=False,
        ),
    ]
