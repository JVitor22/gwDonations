# Generated by Django 3.0.4 on 2020-06-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_delete_itens_doacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='doador',
            name='senha',
            field=models.CharField(default='123456', max_length=50),
        ),
    ]
