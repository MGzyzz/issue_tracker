# Generated by Django 4.2.3 on 2023-07-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0004_project_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
