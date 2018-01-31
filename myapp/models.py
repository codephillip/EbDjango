from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name


class PersonGroup(models.Model):
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person)

    def __unicode__(self):
        return self.name
