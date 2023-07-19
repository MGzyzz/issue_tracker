from django.db import models
from issue_tracker.models.types_and_statuses import Types, Status
from issue_tracker.models.project import Project
# Create your models here.


class Task(models.Model):
    summary = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Summary'
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default='New')
    type = models.ForeignKey(Types, on_delete=models.PROTECT, default='Task')

    time_of_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time of Creation'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='Update time'
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.summary