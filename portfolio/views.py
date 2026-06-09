from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Feedback

def home(request):
    return render(request, 'main/home.html')




from django.shortcuts import render
from .models import Feedback
from django.core.mail import send_mail

def submit_feedback(request):
    if request.method == "POST":
        return render(request, "home.html", {"show_thank_you": True})
    return render(request, "home.html")
 
    
def thank_you(request):
    return render(request, "main/thank_you.html")


