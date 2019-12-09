# Generated by Django 2.2 on 2019-12-09 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratesource',
            name='abbr',
            field=models.CharField(db_index=True, max_length=64, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AddConstraint(
            model_name='ratesource',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, abbr=''), name='rate_source_not_empty_abbr_cst'),
        ),
    ]