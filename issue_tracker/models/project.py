from django.db import models
from issue_tracker.models.types_and_statuses import Types, Status


class Project(models.Model):
    title = models.CharField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(
        null=True, blank=True, verbose_name='End Date'
    )

    users = models.ManyToManyField('accounts.User')

    def __str__(self):
        return self.title