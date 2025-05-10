from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    students = [
        {"id": 1, "name": "Rishav Saha", "age": 27}
    ]
    return HttpResponse(students)