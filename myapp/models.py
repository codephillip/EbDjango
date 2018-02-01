from __future__ import unicode_literals
from django.db import models

import uuid


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name


class PersonGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person)

    def __unicode__(self):
        return self.name
