# Generated by Django 2.2.3 on 2019-10-14 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0011_auto_20191015_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
