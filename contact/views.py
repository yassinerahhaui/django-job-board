from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_message(request):
    info = Info.objects.last()
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER ,
            [email],
        )
    context = {
        'info': info,
    }
    return render(request,'contact/contact.html',context)