# Generated by Django 5.0.3 on 2024-04-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_transaction_date_transaction_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='use_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
