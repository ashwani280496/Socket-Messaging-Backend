# Generated by Django 3.1.5 on 2021-06-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210610_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]