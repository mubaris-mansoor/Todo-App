# Generated by Django 4.0.3 on 2022-11-30 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_todolistitem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='user',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]