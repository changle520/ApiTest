# Generated by Django 3.0.5 on 2020-09-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_db_apis'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_apis',
            name='last_api_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='db_apis',
            name='last_body_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
