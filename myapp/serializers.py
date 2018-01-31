from rest_framework import serializers

from myapp.models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'age', 'name')


class PersonGroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonGroup
        fields = ('id', 'name', 'persons')


class PersonGroupGetSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True, read_only=True)
    
    class Meta:
        model = PersonGroup
        fields = ('id', 'name', 'persons')
