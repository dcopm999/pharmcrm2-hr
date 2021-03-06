# -*- coding: utf-8 -*-
from django.urls import include, path
from django.views.generic import TemplateView

app_name = "hr"
urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
    path("api/", include("hr.api.urls")),
]
