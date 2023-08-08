# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):

    """Модель для хранения информации о подписчиках"""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Newsletter(models.Model):

    """Модель для хранения информации о рассылках"""

    subject = models.CharField(max_length=100)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class EmailLog(models.Model):

    """Модель для записи информации об открытии писем"""

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return self.subscriber.email

