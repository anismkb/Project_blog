
from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.main, name="Index"),
    path('chat', views.index, name="chat"),
]


