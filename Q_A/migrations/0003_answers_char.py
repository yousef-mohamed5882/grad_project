# Generated by Django 3.2.9 on 2022-04-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Q_A', '0002_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='Char',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
    ]