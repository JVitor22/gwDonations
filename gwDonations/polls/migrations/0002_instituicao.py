# Generated by Django 3.0.4 on 2020-04-08 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=256)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
