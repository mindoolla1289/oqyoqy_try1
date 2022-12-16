# Generated by Django 4.1.3 on 2022-12-16 00:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0004_customuser_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                null=True, related_name="CourseStudents", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]