# Generated by Django 2.2.1 on 2020-02-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleblog', '0004_auto_20200218_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.IntegerField(default=0, verbose_name='点击率'),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐'),
        ),
    ]
