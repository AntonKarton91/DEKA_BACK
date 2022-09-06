from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         initials = '33'
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     stages = (
#         ('к', 'конструктор'),
#         ('д', 'дизайнер'),
#         ('м', 'менеджер'),
#     )
#
#     username = None
#     stage = models.CharField(max_length=1, choices=stages)
#     initials = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#
#     def getInitials(self):
#         self.initials = 1
#
#     # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#     #     self.getInitials()
#     #     super().save(self, force_insert=False, force_update=False, using=None, update_fields=None)
#
#     def __str__(self):
#         return self.email

class TableColumns(models.Model):
    TYPE = (
        ('QUEUE', 'Queue'),
        ('WORK', 'Work'),
        ('ARCHIVE', 'Archive'),
    )

    column_name = models.CharField(max_length=255, default='Новая колонка')
    column_type = models.CharField(max_length=200, choices=TYPE)
    column_position = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return f'Column {self.column_name}'


class Tasks(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(max_length=5000)
    column = models.ForeignKey(TableColumns, on_delete=models.CASCADE)
    task_participants = models.ManyToManyField(User, related_name='tasks')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Task {self.task_name}'


