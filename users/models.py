from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Lessons, Courses


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


class Pay(models.Model):
    CASH = 'cash'
    CASH_ACCOUNT = 'cash_account'
    TYPE_PAY = [(CASH, 'наличные'), (CASH_ACCOUNT, 'перевод на счет')]
    user = models.ForeignKey(User, related_name='pays', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, related_name='lessons', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, related_name='courses', on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name='дата оплаты', auto_now=True)
    total_pay = models.PositiveIntegerField(verbose_name='сумма оплаты')
    choose_pay = models.CharField(max_length=20, choices=TYPE_PAY, verbose_name='вид оплаты')

