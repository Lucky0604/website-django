from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Company, Author, Content, CompanyImage
# Create your views here.

def index(request):
    img = CompanyImage.objects.all()
    return render(request, 'index.html', {'img': img})

def main_list(request):
    companys = Company.objects.all()
    contents = Content.objects.all()
    return render(request, 'company/main_list.html', {'companys': companys, 'contents': contents})

def main_detail(request, pk):
    content = get_object_or_404(Content, pk = pk)
    return render(request, 'company/main_detail.html', {'content': content})