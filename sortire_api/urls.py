from django.urls import path
from django.views.generic import TemplateView

app_name = "sortire"

urlpatterns = [
    path("", TemplateView.as_view(template_name="sortire/index.html")),
]