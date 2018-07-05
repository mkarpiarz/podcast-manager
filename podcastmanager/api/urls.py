from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PodcastList

urlpatterns = {
    url(r'^podcasts/$', PodcastList.as_view(), name="list_and_create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
