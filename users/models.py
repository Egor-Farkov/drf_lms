from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Courses, Lessons


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="images/", verbose_name="аватар", null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=20, verbose_name="номер телефона", null=True, blank=True
    )
    city = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Pay(models.Model):
    CASH = "cash"
    CASH_ACCOUNT = "cash_account"
    TYPE_PAY = [(CASH, "наличные"), (CASH_ACCOUNT, "перевод на счет")]
    user = models.ForeignKey(User, related_name="pays", on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lessons,
        related_name="payments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Courses,
        related_name="payments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="дата и время оплаты", auto_now_add=True
    )
    total_pay = models.PositiveIntegerField(verbose_name="сумма оплаты")
    choose_pay = models.CharField(
        max_length=20, choices=TYPE_PAY, verbose_name="вид оплаты"
    )

    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Id сессии",
        help_text="Укажите Id сессии",
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"Платеж {self.id} - {self.user} - {self.total_pay} руб."


class SubscribeCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"Подписка {self.user} - {self.course}"
