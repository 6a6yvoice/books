from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import *
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import ContactForm
from rest_framework import parsers
from rest_framework.views import APIView
#from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

def main(request):
    return render (request, 'main.html')

def reg(request): 
    if request.method == "POST":
        data = request.POST
        newuser = User.objects.create_user(username = data["user"], password = data["password"])
        newuser.save()
        return redirect ("http://127.0.0.1:8000/reg")
    return render(request, 'reg.html')

def auth(request): 
    if request.method == "POST": 
        data = request.POST
        user = authenticate(username = data["user"], password = data["password"] )
        if user is not None:
            request.session['is_auth'] = True
            return redirect
        else:
            return HttpResponse('Пользователь не зарегистрирован')
    return render (request, 'auth.html')

class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение от {data["first_name"]} {data["last_name"]} Почта отправителя {data["email"]}'
        email(subject, data["message"])        
        return super().form_valid(form)

def email(subject, content):
    send_mail(subject, content, 'отправитель@gmail.com', ['получатель@gmail.com'])

def success(request):
    return HttpResponse('Сообщение успешно отправлено!')

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['https://gitlab.grokhotov.ru/hr/yii-test-vacancy/-/raw/master/books.json']
        res = file_obj.text 
        for books in res:
            if books['categories'] == []:
                books['categories'] = ['new']
            print(books['title'], books['categories'])
        return Response(status=204)
