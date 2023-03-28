# Generated by Django 3.2.9 on 2021-12-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_rename_transactions_qr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr',
            name='contact',
        ),
        migrations.AddField(
            model_name='qr',
            name='route',
            field=models.CharField(default='Nairobi-Thika', max_length=50),
            preserve_default=False,
        ),
    ]