# Generated by Django 3.1.7 on 2021-03-03 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('bucket', models.IntegerField(choices=[(1, '1 Day'), (2, '3 Days'), (3, '7 Days'), (4, '16 Days'), (5, '30 Days')], default=1)),
                ('nextReviewAt', models.DateTimeField()),
                ('lastReviwedAt', models.DateTimeField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.deck')),
            ],
        ),
    ]
