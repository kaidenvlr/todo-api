from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название команды')
    members = models.ManyToManyField(User, related_name='team', verbose_name='Участники команды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда разработчиков'
        verbose_name_plural = 'Команды разработчиков'


class TaskLevel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название уровня задачи')
    color = models.CharField(max_length=7, verbose_name='Цвет уровня задачи', help_text='Вводить в формате #FFFFFF')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень задачи'
        verbose_name_plural = 'Уровни задачи'


class TaskList(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название списка задач')
    color = models.CharField(max_length=7, verbose_name='Цвет списка задачи', help_text='Вводить в формате #FFFFFF')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Команда разработчиков')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, verbose_name='Список задач')
    task_level = models.ForeignKey(TaskLevel, on_delete=models.CASCADE, verbose_name='Уровень задачи')
    name = models.CharField(max_length=200, verbose_name='Название задачи')
    is_done = models.BooleanField(default=False, verbose_name='Завершена?')
    date_complete = models.DateField(null=True, blank=True, verbose_name='Дата завершения задачи')
    date_to = models.DateField(null=True, blank=True, verbose_name='Дата ожидаемого завершения задачи')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
