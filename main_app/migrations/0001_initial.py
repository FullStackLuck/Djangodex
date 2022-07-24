# Generated by Django 4.0.6 on 2022-07-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('moves', models.CharField(max_length=100)),
                ('weakness', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=20)),
            ],
        ),
    ]
