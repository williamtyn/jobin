# Generated by Django 3.2.16 on 2022-11-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0006_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='consultants.order'),
        ),
    ]
