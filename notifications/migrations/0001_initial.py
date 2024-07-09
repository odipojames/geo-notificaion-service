# Generated by Django 4.2.13 on 2024-07-08 12:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payload', models.JSONField()),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]
