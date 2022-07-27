# Generated by Django 4.0.6 on 2022-07-27 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Weakness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Weakness 1', 'Normal'), ('Weakness 2', 'Fire'), ('Weakness 3', 'Water'), ('Weakness 4', ' Electric'), ('Weakness 5', 'Grass'), ('Weakness 6', 'Ice'), ('Weakness 7', 'Fighting'), ('Weakness 8', 'Poison'), ('Weakness 9', 'Ground'), ('Weakness 10', 'Flying'), ('Weakness 11', 'Psychic'), ('Weakness 12', 'Bug'), ('Weakness 13', 'Rock'), ('Weakness 14', 'Ghost'), ('Weakness 15', 'Dragon'), ('Weakness 16', 'Dark'), ('Weakness 17', 'Steel'), ('Weakness 18', 'Fairy')], default='Weakness 1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('attack', models.IntegerField(max_length=3)),
                ('defense', models.IntegerField(max_length=3)),
                ('specialatk', models.IntegerField(max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Type 1', 'Medicine'), ('Type 2', 'Battle Item'), ('Type 3', 'General Item'), ('Type 4', ' Hold Item'), ('Type 5', ' Machine'), ('Type 6', 'Artifact')], default='Type 1', max_length=50)),
                ('name', models.CharField(choices=[('Berry 1', 'Aguav Berry'), ('Berry 2', 'Apicot Berry'), ('Berry 3', 'Aspear Berry'), ('Berry 4', ' Babiri Berry'), ('Berry 5', 'Charti Berry'), ('Battle 6', 'XAttack'), ('Battle 7', 'Reset Urge'), ('Battle 8', 'Sassy Mint'), ('Battle 9', 'Relaxed Mint'), ('Battle 10', 'Guard Spec.'), ('Battle 11', 'Brave Mint'), ('Hold 12', 'Black Belt'), ('Hold 13', 'Assualt Vest'), ('Hold 14', 'Air Ballon'), ('Hold 15', 'Absolite'), ('Machine 16', 'HM04'), ('Machine 17', 'HM03'), ('Machine 18', 'HM02'), ('Machine 19', 'HM01'), ('Machine 20', 'Lansat Berry'), ('Medicine 21', 'Clever Wing'), ('Medicine 22', 'Calcium'), ('Medicine 23', 'Burn Heal'), ('Medicine 24', 'Awakening'), ('Medicine 25', 'Antidote'), ('Berry 19', 'Jaboca Berry'), ('Berry 20', 'Lansat Berry'), ('Berry 21', 'Liechi Berry'), ('Berry 22', 'Maranga Berry'), ('Berry 23', 'Pamtre Berry'), ('Berry 24', 'Payapa Berry'), ('Berry 25', 'Kelpsy Berry')], default='Berry 1', max_length=50)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
    ]
