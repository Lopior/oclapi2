# Generated by Django 3.0.9 on 2020-12-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='logo_path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
