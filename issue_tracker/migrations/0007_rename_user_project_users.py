# Generated by Django 4.2.3 on 2023-07-29 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0006_project_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='users',
        ),
    ]