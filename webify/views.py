from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')
def workflow(request):
    return render(request, 'workflow.html')
def casestudy(request):
    return render(request, 'case_studies.html')
def about(request):
    return render(request, 'about.html')