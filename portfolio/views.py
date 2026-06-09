from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Feedback

def home(request):
    return render(request, 'main/home.html')




from django.shortcuts import render
from django.core.mail import send_mail
from .models import Feedback

def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save feedback to database
        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email notification (safe mode)
        send_mail(
            "New Feedback Received",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            "jaganathmk2020.mgce@gmail.com",   # sender
            ["jaganathmk2020.mgce@gmail.com"], # recipient
            fail_silently=True
        )

        # Render thank-you alert
        return render(request, "main/home.html", {"show_thank_you": True})

    return render(request, "main/home.html")

 
    
def thank_you(request):
    return render(request, "main/thank_you.html")


