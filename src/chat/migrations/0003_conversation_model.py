# Generated by Django 4.1.5 on 2023-01-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_answer_conversation_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
