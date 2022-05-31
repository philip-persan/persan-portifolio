from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render


def contact_view(request):
    return render(request, 'contact/pages/contact.html')


def contact_send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

    send_mail(subject + ' : ' + name, message, email)

    messages.success(request, 'E-mail Sent!')
    return render(request, 'contact/pages/contact.html')
