from django.contrib import admin
from .models import Task, Benefactor, Charity

admin.site.register(Charity)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'gender_limit')
    list_editable = ('state', 'gender_limit')
    list_display_links = ('title',)


@admin.register(Benefactor)
class BenefactorAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience')
    list_editable = ('experience',)
    list_display_links = ('user',)