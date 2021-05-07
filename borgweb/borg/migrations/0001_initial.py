# Generated by Django 3.2 on 2021-05-07 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.TextField()),
                ('name', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('file_count', models.IntegerField()),
                ('original_size', models.IntegerField()),
                ('compressed_size', models.IntegerField()),
                ('deduplicated_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.TextField(unique=True)),
                ('location', models.TextField()),
                ('last_modified', models.DateTimeField()),
                ('label', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='borg.label')),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField()),
                ('time', models.DateTimeField()),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='borg.label')),
            ],
        ),
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_chunks', models.IntegerField()),
                ('total_csize', models.IntegerField()),
                ('total_size', models.IntegerField()),
                ('total_unique_chunks', models.IntegerField()),
                ('unique_csize', models.IntegerField()),
                ('unique_size', models.IntegerField()),
                ('archive', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='borg.archive')),
            ],
        ),
        migrations.AddField(
            model_name='archive',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archives', to='borg.repo'),
        ),
    ]
