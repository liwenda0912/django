# Generated by Django 4.0.6 on 2022-07-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0006_taobao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taobao',
            name='num',
            field=models.IntegerField(max_length=10, verbose_name='月售'),
        ),
    ]
