from __future__ import unicode_literals

from django.conf.urls import url

from yacms.generic import views


urlpatterns = [
    url("^rating/$", views.rating, name="rating"),
    url("^comment/$", views.comment, name="comment"),
]
