# Generated by Django 3.2 on 2021-05-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField(unique=True)),
                ('path', models.TextField()),
                ('last_checked', models.DateTimeField(null=True)),
            ],
        ),
    ]
