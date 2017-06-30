from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from medibot import views

urlpatterns = [
    url(r'^medibot/$', views.MedibotView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
