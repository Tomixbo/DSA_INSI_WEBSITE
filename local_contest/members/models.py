from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GRADUATION_CHOICES = [
        ('L1_v1', 'L1_v1'),
        ('L1_v2', 'L1_v2'),
        ('L2_IAD', 'L2_IAD'),
        ('L2_GL', 'L2_GL'),
        ('L2_ARSB', 'L2_ARSB'),
    ]
    CATEGORY_CHOICES = [
        ('Alpha', 'Alpha'),
        ('Beta', 'Beta'),
        ('Gamma', 'Gamma'),
        ('Omega', 'Omega'),
    ]
    graduation_field = models.CharField(max_length=10, choices=GRADUATION_CHOICES, default='L1_v1')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Alpha')

    rank = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    