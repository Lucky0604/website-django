from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Company, Author, Content
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def main_list(request):
    companys = Company.objects.all()
    contents = Content.objects.all()
    return render(request, 'company/main_list.html', {'companys': companys, 'contents': contents})