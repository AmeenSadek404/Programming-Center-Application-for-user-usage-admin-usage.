# Generated by Django 2.2.3 on 2019-10-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0015_auto_20191015_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(default='amin', max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(default='amin', max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='second_name',
            field=models.CharField(default='amin', max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='third_name',
            field=models.CharField(default='amin', max_length=50),
        ),
    ]
