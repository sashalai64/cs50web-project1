from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name = "entry"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/new/", views.new, name="new"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
]
