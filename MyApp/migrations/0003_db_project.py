# Generated by Django 3.0.5 on 2020-09-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_db_home_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('remark', models.CharField(max_length=1000, null=True)),
                ('user', models.CharField(max_length=15, null=True)),
                ('other_users', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
