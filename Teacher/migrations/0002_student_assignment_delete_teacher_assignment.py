# Generated by Django 5.1.3 on 2025-06-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Email', models.CharField(max_length=200)),
                ('Subject_Name', models.CharField(max_length=200)),
                ('Assignment_Title', models.CharField(max_length=200)),
                ('Assignment_Description', models.CharField(max_length=200)),
                ('File_Name', models.CharField(max_length=200)),
                ('Submission_Date', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher_Assignment',
        ),
    ]
