from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.ObsQueueView, name="dashboard"),
    path("observed/<int:pk>", views.observed, name="observed"),
    path("surveyfields/", views.SurveyFieldsView, name="surveyfields"),
]
