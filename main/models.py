from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


from main.model_managers import CustomUserManager


def upload(instance, filename):
    return f'Avatars/ava_for_{instance}_{filename}'

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    url = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    initials = models.CharField(max_length=255, blank=True)
    ava = models.ImageField(upload_to=upload, default='Avatars/unknown_user.jpg', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



    def save(self, *args, **kwargs):
        if not self.initials:
            self.initials = self.first_name.upper()[0] + self.last_name.upper()[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class TableColumns(models.Model):
    TYPE = (
        ('QUEUE', 'Queue'),
        ('WORK', 'Work'),
        ('ARCHIVE', 'Archive'),
    )

    columnName = models.CharField(max_length=255, default='Новая колонка')
    columnType = models.CharField(max_length=200, choices=TYPE)
    columnPosition = models.IntegerField(blank=True, null=True)
    order = models.CharField(max_length=255, default=[])

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return f'Column {self.columnName}'

class Marks(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

    def __str__(self):
        return f'Task {self.title}'

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    taskDescription = models.TextField(max_length=5000, null=True, blank=True)
    column = models.ForeignKey(TableColumns,
                               on_delete=models.CASCADE,
                               related_name='tasks',
                               blank=True,
                               null=True)
    participants = models.ManyToManyField(CustomUser, related_name='parts', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    taskPosition = models.IntegerField(blank=True, null=True)
    marks = models.ManyToManyField(Marks, related_name='marks', blank=True, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Task {self.name}'




class TaskComments(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='task_comment')
    creater = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creater')
    createDate = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
