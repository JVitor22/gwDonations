# Generated by Django 3.0.7 on 2020-06-10 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200610_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='imagem',
            field=models.CharField(default='', max_length=200),
        ),
    ]
