from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from clientes.models import Cliente
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from threading import Thread
from . import settings


class Index(generic.View):

    def get(self, request):

        return render(request, 'index.html', {

        })

    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if Cliente.objects.filter(email=email).count() == 0:
            Cliente.objects.create(name=name, email=email, phone=phone)
            messages.success(request, 'Gracias por enviarnos tu información, pronto nos estarémos poniendo en contacto contigo')
            send_email_to_me(name_client=name, email_client=email, phone_client=phone)
            send_email_to_client(name_client=name, email_client=email)
            return redirect('index')
        
        else:
            messages.error(
                request, 'Tu correo electrónico ya se encuentra registrado')
            return redirect('index')

        return redirect('index')

def send_email(email, content):
    email.attach_alternative(content, 'text/html')
    email.send()

def send_email_to_client(name_client, email_client):
    context = {
        'name': name_client,
        'email': email_client,
    }

    template = get_template('email-to-client.html')

    content = template.render(context)

    email = EmailMultiAlternatives(
        'Hola {}, te saluda Richi'.format(name_client),
        'landing-solar-panels',
        settings.EMAIL_HOST_USER,
        [email_client]
    )

    Thread(target=send_email, args=(email, content)).start()


def send_email_to_me(name_client, email_client, phone_client):
    
    context = {
        'name': name_client,
        'email': email_client,
        'phone': phone_client,
    }

    template = get_template('email-from-form.html')

    content = template.render(context)

    email = EmailMultiAlternatives(
        # select is the subject on the form
        '{} ahora es un cliente'.format(name_client),
        'landing-solar-panels',
        settings.EMAIL_HOST_USER,
        ['10xpowur@gmail.com']
    )

    Thread(target=send_email, args=(email, content)).start()