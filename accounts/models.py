from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Gender_Choices = [
        ('M', 'male'),
        ('F', 'female'),
    ]

    address = models.TextField(blank = True, null = True)
    age = models.PositiveSmallIntegerField(blank = True, null = True)
    date_joined = models.DateTimeField(AbstractUser)
    description = models.TextField(blank = True, null = True)
    email = models.EmailField(AbstractUser, blank = True, null = True)
    first_name = models.CharField(AbstractUser, max_length = 100,blank = True, null = True)
    gender = models.CharField(
        AbstractUser,
        max_length = 1,
        choices = Gender_Choices, 
        blank = True, null = True
        )
    is_active = models.BooleanField(AbstractUser, default = True)
    is_staff = models.BooleanField(AbstractUser, default = False)
    is_superuser = models.BooleanField(AbstractUser, default = False)
    last_login = models.DateTimeField(AbstractUser, blank = True, null = True)
    last_name = models.CharField(AbstractUser, max_length = 100, blank = True, null = True)
    password = models.CharField(AbstractUser, max_length = 100)
    phone = models.CharField(AbstractUser, max_length = 15, blank = True, null = True)
    username = models.CharField(AbstractUser, max_length = 100, unique = True)
