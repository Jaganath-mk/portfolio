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
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(name=name, email=email, message=message)

        # Send email notification
        subject = "New Feedback Submitted"
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        send_mail(subject, body, 'yourgmail@gmail.com', ['yourgmail@gmail.com'])

        return render(request, "main/home.html", {"show_thank_you": True})

    return render(request, "main/home.html")
 
    
def thank_you(request):
    return render(request, "main/thank_you.html")


