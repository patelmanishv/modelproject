# Generated by Django 4.2.4 on 2023-08-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(upload_to="profilepics/"),
        ),
    ]
