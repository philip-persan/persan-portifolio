from django.db import models


class SoftSkill(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Soft Skills',
        blank=False
    )

    def __str__(self):
        return self.name


class HardSkill(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Hard Skills',
        blank=False
    )

    def __str__(self):
        return self.name
