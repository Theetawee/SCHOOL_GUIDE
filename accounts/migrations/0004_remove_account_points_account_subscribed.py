# Generated by Django 5.0.3 on 2024-04-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='points',
        ),
        migrations.AddField(
            model_name='account',
            name='subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
