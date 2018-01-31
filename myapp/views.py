from __future__ import unicode_literals
from rest_framework.generics import ListCreateAPIView
from myapp.models import *
from myapp.serializers import *


class PersonView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonGroupView(ListCreateAPIView):
    queryset = PersonGroup.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PersonGroupPostSerializer
        else:
            return PersonGroupGetSerializer
