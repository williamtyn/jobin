# Generated by Django 3.2.16 on 2022-11-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0004_auto_20221122_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Customer'), (1, 'Partner')], default=0),
        ),
    ]
