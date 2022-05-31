from django.db import models


class Experience(models.Model):
    enterprise = models.CharField(
        max_length=70,
        verbose_name='Enterprise/Company',
        blank=False,
        null=True
    )
    position = models.CharField(
        max_length=70,
        verbose_name='Position',
        blank=False,
        null=True
    )
    started_at = models.DateField(
        verbose_name='Started at',
        auto_now=False,
        blank=False,
        null=True
    )
    finished_at = models.DateField(
        verbose_name='Finished at',
        auto_now=False,
        blank=True,
        null=True
    )
    is_on = models.BooleanField(
        verbose_name='Still Working?',
        default=True
    )

    def __str__(self):
        return self.position
