# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import loader

from .models import Newsletter, Subscriber


@shared_task
def send_newsletter_with_variables(newsletter, recipients):
    for recipient_email, variables in recipients:

        html_template = loader.get_template('emailer/newsletter_template.html')

        html_content = html_template.render(variables)

        email = EmailMultiAlternatives(newsletter.subject, '', 'sayapov2000@yandex.ru', [recipient_email])
        email.attach_alternative(html_content, 'text/html')
        email.send()

