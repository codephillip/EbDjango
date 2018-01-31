from django.conf.urls import url
from django.contrib import admin

from myapp.views import PersonView, PersonGroupView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/v1/persons$', PersonView.as_view(), name='persons'),
    url(r'api/v1/persons_groups$', PersonGroupView.as_view(), name='persons_groups'),
]
