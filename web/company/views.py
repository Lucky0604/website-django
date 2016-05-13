from django.shortcuts import render
from django.utils import timezone
from .models import Company, Author, Content
# Create your views here.

def company_list(request):
    tags = Company.objects.all()
    return render(request, 'company/company_list.html', {'tags': tags})

def post_list(request):
    contents = Content.objects.all()
    return render(request, 'company/post_list.html', {'posts': posts})
