# Generated by Django 5.0.3 on 2024-04-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_account_subscribed_account_last_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]