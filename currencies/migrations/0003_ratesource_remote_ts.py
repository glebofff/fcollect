# Generated by Django 3.0 on 2019-12-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_log_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratesource',
            name='remote_ts',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]