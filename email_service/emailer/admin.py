# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from emailer.models import *

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Newsletter)
admin.site.register(EmailLog)