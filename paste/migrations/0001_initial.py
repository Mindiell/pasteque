# Generated by Django 2.0.5 on 2018-05-06 13:00

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Paste",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(editable=False, unique=True)),
                ("title", models.CharField(blank=True, max_length=200)),
                (
                    "content",
                    models.TextField(
                        validators=[django.core.validators.MaxLengthValidator(100000)]
                    ),
                ),
                ("size", models.IntegerField(default=0, editable=False)),
                (
                    "paste_time",
                    models.DateTimeField(default=datetime.datetime.now, editable=False),
                ),
                ("paste_ip", models.GenericIPAddressField(editable=False)),
                ("paste_agent", models.CharField(editable=False, max_length=200)),
                (
                    "lifetime",
                    models.IntegerField(
                        choices=[
                            (0, "Never expire"),
                            (5, "5 minutes"),
                            (30, "30 minutes"),
                            (60, "1 hour"),
                            (1440, "1 day"),
                            (10080, "1 week"),
                        ],
                        default=0,
                    ),
                ),
                ("lifecount", models.IntegerField(default=0)),
                ("viewcount", models.IntegerField(default=0, editable=False)),
                ("expired", models.BooleanField(default=False, editable=False)),
                ("private", models.BooleanField(default=False)),
                ("password", models.CharField(blank=True, max_length=128)),
                ("salt", models.CharField(blank=True, max_length=36)),
                (
                    "language",
                    models.ForeignKey(
                        default=13,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="paste.Language",
                    ),
                ),
            ],
        ),
    ]
