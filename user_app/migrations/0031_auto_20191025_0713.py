# Generated by Django 2.2.3 on 2019-10-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0030_course_course_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_dep',
            field=models.CharField(max_length=150),
        ),
    ]
