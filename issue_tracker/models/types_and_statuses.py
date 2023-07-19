from django.db import models


# Create your models here.

class Types(models.Model):
    name = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Types'
    )

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Status'
    )

    def __str__(self):
        return self.name