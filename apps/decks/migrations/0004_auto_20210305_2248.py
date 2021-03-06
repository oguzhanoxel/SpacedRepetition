# Generated by Django 3.1.7 on 2021-03-05 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0003_auto_20210305_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deck',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
