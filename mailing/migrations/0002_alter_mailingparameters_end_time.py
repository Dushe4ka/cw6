# Generated by Django 5.0.7 on 2024-07-12 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailingparameters",
            name="end_time",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 13, 9, 40, 32, 176824, tzinfo=datetime.timezone.utc
                ),
                verbose_name="конец рассылки",
            ),
        ),
    ]
