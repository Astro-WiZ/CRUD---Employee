# Generated by Django 5.1 on 2024-09-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('eID', models.IntegerField()),
                ('designation', models.CharField(default=None, max_length=50)),
                ('address', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('salary', models.FloatField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
