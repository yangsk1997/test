# Generated by Django 2.2.1 on 2020-02-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者姓名')),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男')], verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='类型名字')),
                ('description', models.TextField(verbose_name='描述')),
            ],
            options={
                'db_table': 'type',
            },
        ),
    ]
