from django.shortcuts import render
from django.utils import timezone
from .models import Company, Author, Content
# Create your views here.

def main_list(request):
    companys = Company.objects.all()
    contents = Content.objects.all()
    return render(request, 'company/main_list.html', {'companys': companys, 'contents': contents})
