# Generated by Django 4.0.3 on 2022-11-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_remove_todolistitem_content_todolistitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='content',
            field=models.TextField(default='ghgtfdsf'),
            preserve_default=False,
        ),
    ]
