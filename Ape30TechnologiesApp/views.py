from django.shortcuts import render
from django.core.mail import send_mail


def Home(request):
    return render (request, 'home.html')

def ContactUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phone']
        message = request.POST['message']

        # send mail
        send_mail(
            "Contact form submission at Ape 30 Technologies Website",  # subject
            message + "\n" "\n" "\n" "Name : " + name + "\n" "Phone number : " + phoneNumber + "\n" "Email : " + email,  # message
            'ape30technologies@gmail.com',  # from email
            ['ape30technologies@gmail.com'],  # to email
        )
        return render(request, "contactUs.html", {
            "name": name
        })
    else:
        return render(request, "contactUs.html")

def HireUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']

        # send mail
        send_mail(
            "Contact form submission at Ape 30 Technologies Website",  # subject
            message + "\n" "\n" "\n" "Name : " + name + "\n" "Phone number : " + phoneNumber + "\n" "Email : " + email,  # message
            'ape30technologies@gmail.com',  # from email
            ['ape30technologies@gmail.com'],  # to email
        )
        return render(request, "hireUs.html", {
            "name": name
        })
    else:
        
        return render (request, 'hireUs.html')

def MobileApps(request):
    return render (request, 'mobileApps.html')