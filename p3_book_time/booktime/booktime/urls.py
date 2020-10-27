
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    # path("", TemplateView.as_view(template_name="home.html")),
    # path("about/", TemplateView.as_view(template_name="about.html"))
]
