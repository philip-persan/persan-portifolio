from django.db import models


class Education(models.Model):
    school = models.CharField(
        max_length=70,
        verbose_name='School/Campus',
        blank=False,
        null=True
    )
    education_level = models.CharField(
        max_length=70,
        verbose_name='Education Level',
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
        blank=False,
        null=True
    )
    completed = 'Completed'
    studying = 'Studying'
    stopped = 'Stopped'
    CHOICES = [
        (completed, 'Completed'),
        (studying, 'Studying'),
        (stopped, 'Stopped'),
    ]
    status = models.CharField(
        max_length=30,
        choices=CHOICES,
        blank=False,
        null=True
    )

    def __str__(self):
        return self.school
