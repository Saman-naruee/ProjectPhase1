from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    EXPERIENCE_CHOICES = [
            (1, 'Beginner'),
            (2, 'Intermediate'),
            (3, 'Expert'),
        ]

    # id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices = EXPERIENCE_CHOICES, default = 1)
    free_time_per_week = models.PositiveSmallIntegerField(default = 0)


class Charity(models.Model):
    # id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    reg_name = models.CharField(max_length = 10)


class Task(models.Model):
    Gender_Choices = [
        ('M', 'male'),
        ('F', 'female'),
    ]

    States = [
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    ]

    # id = models.AutoField(null=False)
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete = models.CASCADE)
    age_limit_from = models.IntegerField(blank = True, null = True)
    age_limit_to = models.IntegerField(blank = True, null = True)
    date = models.DateField(null = True, blank = True)
    description = models.TextField(blank = True, null = True)
    title = models.CharField(max_length = 60)
    state = models.CharField(max_length = 1, choices = States, default = 'M')
    gender_limit = models.CharField(max_length = 1, choices = Gender_Choices)
