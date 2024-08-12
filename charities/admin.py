from django.contrib import admin
from .models import Task, Benefactor, Charity

admin.site.register(Task)
admin.site.register(Benefactor)
admin.site.register(Charity)
