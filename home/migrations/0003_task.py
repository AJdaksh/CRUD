# Generated by Django 4.0.4 on 2022-04-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktitle', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=122)),
            ],
        ),
    ]
