import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class Owner(AbstractUser):
    profession = models.CharField(max_length=60, verbose_name='Profession')
    degree = models.CharField(max_length=60, verbose_name='Degree')
    location = models.CharField(
        max_length=255,
        verbose_name='City, State/Country'
    )
    phone = models.CharField(max_length=30, verbose_name='Phone')
    freelance = models.BooleanField(
        verbose_name='Freelance',
        null=True,
        default=True
    )
    open_to_work = models.BooleanField(
        verbose_name='Open to Work',
        null=True,
        default=True
    )
    birthday = models.DateField(
        verbose_name='Birthday',
        auto_now=False,
        auto_created=False,
        null=True
    )

    @property
    def age(self):
        if(self.birthday is not None):
            age = datetime.date.today().year - self.birthday.year
            return age
