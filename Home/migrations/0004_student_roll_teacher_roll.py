# Generated by Django 5.1.3 on 2025-06-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Roll',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Roll',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
