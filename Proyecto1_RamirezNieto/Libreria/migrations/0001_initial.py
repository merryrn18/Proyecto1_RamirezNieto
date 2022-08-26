# Generated by Django 4.1 on 2022-08-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('duracion', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('escritor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Revistas',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('editorial', models.CharField(max_length=100)),
            ],
        ),
    ]