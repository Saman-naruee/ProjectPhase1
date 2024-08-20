from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    EXPERIENCE_CHOICES = [
            (1, 'Beginner'),
            (2, 'Intermediate'),
            (3, 'Expert'),
        ]
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices = EXPERIENCE_CHOICES, default = 1)
    free_time_per_week = models.PositiveSmallIntegerField(default = 0)

    def __str__(self) -> str:
        return f'benefactor for : {self.user.username}'


class Charity(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    reg_number = models.CharField(max_length = 10, default = '')

    def __str__(self) -> str:
        return f'charity for : {self.user.username}'


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        try:
            charity = Charity.objects.get(user=user)
        except Charity.DoesNotExist:
            return self.none()
        return super().get_queryset().filter(charity=charity)

    def related_tasks_to_benefactor(self, user):
        try:
            benefactor = Benefactor.objects.get(user=user)
        except Benefactor.DoesNotExist:
            return self.none()
        return super().get_queryset().filter(assigned_benefactor=benefactor)

    def all_related_tasks_to_user(self, user):
        return self.related_tasks_to_charity(user) | self.related_tasks_to_benefactor(user) | super().get_queryset().filter(state='P')

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
    assigned_benefactor = models.ForeignKey(Benefactor, null = True, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete = models.CASCADE)
    age_limit_from = models.IntegerField(blank = True, null = True)
    age_limit_to = models.IntegerField(blank = True, null = True)
    date = models.DateField(null = True, blank = True)
    description = models.TextField(blank = True, null = True)
    title = models.CharField(max_length = 60)
    state = models.CharField(max_length = 1, choices = States, default = 'P')
    gender_limit = models.CharField(max_length = 1, choices = Gender_Choices)

    objects = TaskManager()
    task_manager = TaskManager()

    def __str__(self) -> str:
        return f'Task{self.pk}: {self.title}'
