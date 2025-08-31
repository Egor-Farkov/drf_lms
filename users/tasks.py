from datetime import datetime

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def user_active_period():
    users = User.objects.filter(is_superuser=False).all()

    for user in users:
        time_delta = datetime.now() - user.last_login

        if time_delta.days > 30:
            user.is_active = False
            user.save()


@shared_task
def send_subscribe_user_course(theme, email, message):
    send_mail(subject=theme, message=message, recipient_list=[email], from_email=EMAIL_HOST_USER)
