# Generated by Django 3.1.7 on 2021-03-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20210305_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last_reviwed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='next_review_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]