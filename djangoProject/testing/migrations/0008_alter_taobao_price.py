# Generated by Django 4.0.6 on 2022-07-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_alter_taobao_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taobao',
            name='price',
            field=models.FloatField(max_length=10, verbose_name='价格'),
        ),
    ]