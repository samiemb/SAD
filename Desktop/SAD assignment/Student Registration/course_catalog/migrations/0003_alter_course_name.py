# Generated by Django 5.1.2 on 2024-10-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_catalog', '0002_remove_course_credits_remove_course_instructor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='Unnamed Course', max_length=255),
        ),
    ]