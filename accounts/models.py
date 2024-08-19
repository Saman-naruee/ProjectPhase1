from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    Gender_Choices = [
        ('M', 'male'),
        ('F', 'female'),
    ]
    address = models.TextField(blank = True, null = True)
    age = models.PositiveSmallIntegerField(blank = True, null = True)
    date_joined = models.DateTimeField(default = timezone.now, null = False)
    description = models.TextField(blank = True, null = True)
    gender = models.CharField(max_length = 1, choices = Gender_Choices, blank = True, null = True)
    phone = models.CharField(max_length = 15, blank = True, null = True)
    username = models.CharField(max_length=100, unique=True, blank = False, null = False, verbose_name="User Name")
    email = models.EmailField(unique=False, blank = True, null = True, verbose_name="Email Address")
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Last Name")
    password = models.CharField(max_length=128,blank = False, null = False, verbose_name="Password")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")
    is_superuser = models.BooleanField(default=False, verbose_name="Is Superuser")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="Last Login")