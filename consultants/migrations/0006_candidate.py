# Generated by Django 3.2.16 on 2022-11-23 09:26

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0005_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('cv', cloudinary.models.CloudinaryField(max_length=255, verbose_name='cv')),
                ('offer', cloudinary.models.CloudinaryField(max_length=255, verbose_name='offer')),
                ('presented_date', models.DateField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presented_candidates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['presented_date', 'manager'],
            },
        ),
    ]