# Generated by Django 5.1.7 on 2025-04-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0005_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='outreach',
            name='location',
            field=models.CharField(default='Unknown Location', max_length=100),
        ),
    ]
