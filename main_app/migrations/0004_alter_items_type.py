# Generated by Django 4.0.6 on 2022-07-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_items_moves_weakness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='type',
            field=models.CharField(choices=[('Type 1', 'Medicine'), ('Type 2', 'Battle Item'), ('Type 3', 'General Item'), ('Type 4', ' Hold Item'), ('Type 5', ' Machine'), ('Type 6', 'Artifact')], default='Type 1', max_length=50),
        ),
    ]
