from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name' : 'Nishant Nayan', 'age' : 12},
        {'name' : 'Sushmita', 'age' : 11},
        {'name' : 'Seema Mallik', 'age' : 53},
        {'name' : 'Narendra', 'age' : 58},
    ]
    return render(request, "base.html", context = {'peoples' : peoples})

# Create your views here.
