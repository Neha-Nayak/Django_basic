from django.shortcuts import render
# to execute type "python manage.py runserver"
# Create your views here.
from django.http import HttpResponse
# def welcome(request):
#     return HttpResponse("Welcome to Django")
#
# def profile(request):
#     return HttpResponse("student")

# when using html templates
from django.http import HttpResponse
def welcome(request):
    return render(request, 'template.html', {'titles': 'Django', 'link': 'http://127.0.0.1:8000/'})

def profile(request):
    return render(request, 'template.html', {'titles': 'Profile', 'link': 'http://127.0.0.1:8000/'})
#
# def expression(request):
#     a = int(request.GET['text1'])
#     b = int(request.GET['text2'])
#     c = a*b
#     return render(request, 'output.html', {'result': c})

def expression(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a*b
    return render(request, 'output.html', {'result': c})
