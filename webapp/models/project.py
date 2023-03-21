from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    models.ForeignKey(
        to='webapp.Task',
        verbose_name='Проект',
        related_name='projects',
        on_delete=models.CASCADE
    )
    start_date = models.DateField(verbose_name='Дата начала', null=False, blank=False)
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    title = models.CharField(verbose_name='Название проекта', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2500, null=True, blank=True)
    author = models.ManyToManyField(
        through='UserProject',
        to=User,
        related_name='projects',
        verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f"{self.title} - {self.pk}"


class UserProject(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='user_project',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name='project_user',
        verbose_name='Проект',
        on_delete=models.CASCADE
    )
