# Generated by Django 3.0.8 on 2020-09-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(blank=True),
        ),
    ]
