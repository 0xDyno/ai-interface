# Generated by Django 4.1.5 on 2023-03-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_chatmodel_last_usage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmodel',
            old_name='last_usage',
            new_name='last_used',
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='total_used',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
