# Generated by Django 3.1 on 2021-01-27 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=48)),
                ('time', models.DateTimeField()),
                ('author', models.CharField(max_length=48)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=48)),
                ('time', models.DateTimeField()),
                ('author', models.CharField(max_length=48)),
                ('content', models.TextField()),
            ],
        ),
    ]
