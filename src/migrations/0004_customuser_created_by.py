# Generated by Django 4.1.3 on 2022-12-15 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0003_alter_customuser_is_student_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="СоздательСтудента"
            ),
        ),
    ]
