from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path("submit-feedback/", views.submit_feedback, name="submit_feedback"),
    path("thank-you/", views.thank_you, name="thank_you"),

    
]