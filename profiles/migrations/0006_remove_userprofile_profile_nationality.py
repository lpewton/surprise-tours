# Generated by Django 3.2.19 on 2023-07-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_review_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_nationality',
        ),
    ]
