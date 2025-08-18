from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='images/', verbose_name='аватар', null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name='номер телефона', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):

        return self.email