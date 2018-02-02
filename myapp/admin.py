# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myapp.models import *

admin.site.register(Person)
admin.site.register(PersonGroup)
admin.site.register(Ingredient)
admin.site.register(Category)
