from django.shortcuts import render

def home(request):
    return render(request, template_name='home.html')

def contacts(requests):
    return render(request, template_name='contacts.html')

