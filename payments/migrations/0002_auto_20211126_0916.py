# Generated by Django 3.2.9 on 2021-11-26 06:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
