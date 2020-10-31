from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name='signup'),
    path("log_out/", views.log_out, name='log_out'),
    path("", views.home, name='home'),
    path("mylodos/", views.mytodos, name='mytodos')
]
