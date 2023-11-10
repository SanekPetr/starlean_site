from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from products.models import Person
# Create your views here.
def get_all(request:HttpRequest)->HttpResponse:
    all_persons = Person.objects.all()
    return render(request, "persons.html", context={"persons":all_persons})