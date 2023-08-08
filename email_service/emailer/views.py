# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import render_to_string

from emailer.forms import NewsletterForm
from models import Newsletter, Subscriber, EmailLog
from tasks import send_newsletter_with_variables


def create_newsletter(request):

    """Представление для создания рассылки"""

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            return JsonResponse({'success': True, 'newsletter_id': newsletter.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = NewsletterForm()

    return render(request, 'emailer/create_newsletter.html', {'form': form})


def send_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.save()

            # Получаем список подписчиков
            subscribers = Subscriber.objects.all()

            # Создаем список с получателями и переменными
            recipients = []
            for subscriber in subscribers:
                # Переменные для каждого подписчика
                variables = {
                    'name': subscriber.name,
                    'last_name': subscriber.last_name,
                    'birthday': subscriber.email,
                }

                # Добавьте получателя и переменные в список
                recipients.append((subscriber.email, variables))

            # Рендеринг макета рассылки
            email_content = render_to_string('emailer/email_test.html', {'content': newsletter.content})

            # Отправка рассылки с использованием email_content и списка получателей
            send_newsletter_with_variables(email_content, recipients)

            return redirect('subscribers')
    else:
        form = NewsletterForm()

    newsletters = Newsletter.objects.all()  # получение списка рассылок
    return render(request, 'emailer/send_newsletter.html', {'form': form, 'newsletters': newsletters})


def subscribers(request):

    """Представление для отображения списка подписчиков"""

    subscribers = Subscriber.objects.all()
    return render(request, 'emailer/subscribers.html', {'subscribers': subscribers})


def newsletter_stat(request, newsletter_id):

    """Представление для отображения статистики"""

    newsletter = Newsletter.objects.get(id=newsletter_id)
    opens = EmailLog.objects.filter(newsletter=newsletter)
    return render(request, 'emailer/newsletter_stat.html', {'newsletter': newsletter, 'opens': opens})


def open_track(request, newsletter_id):

    """Представление для отслеживания письма"""

    if 'subscriber' in request.GET:
        subscriber_id = request.GET['subscriber']
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subscriber = Subscriber.objects.get(id=subscriber_id)
        log, created = EmailLog.objects.get_or_create(newsletter=newsletter, subscriber=subscriber)

        if created:
            return JsonResponse({'success': True, 'message': 'Email logged successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Email already logged'})
    else:
        return JsonResponse({'success': False, 'message': 'Subscriber not found'})


def ajax_create_newsletter(request):
    if request.is_ajax() and request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            return JsonResponse({'success': True, 'newsletter_id': newsletter.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'success': False, 'errors': 'Invalid request'})
