from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    picture = models.ImageField(upload_to='images/', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)


class Lessons(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    picture = models.ImageField(upload_to='images/', verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    url_video = models.TextField(verbose_name='ссыдка на видео', null=True, blank=True)
    course = models.ForeignKey(Courses, related_name='lessons', on_delete=models.CASCADE)


