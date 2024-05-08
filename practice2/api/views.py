from django.shortcuts import render

# Create your views here.
def stud_list(request):
    students = ['Aman', 'Aibek', 'Aydar', 'Birzhan']
    return render(request, 'index.html', {"students":students})