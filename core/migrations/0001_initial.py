# Generated by Django 4.2.7 on 2023-11-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_emergencia', models.IntegerField()),
                ('numero_paciente', models.IntegerField()),
                ('contexto_emergencia', models.CharField(max_length=200)),
                ('tipo_emergencia', models.CharField(max_length=100)),
            ],
        ),
    ]
