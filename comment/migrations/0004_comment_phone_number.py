# Generated by Django 3.2 on 2021-04-16 07:48

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_comment_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
