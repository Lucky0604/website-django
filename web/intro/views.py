from django.shortcuts import render
from .models import Content, Company
# Create your views here.
def intro_main(request):
    contents = Content.objects.all()
    companys = Company.objects.all()
    return render(request, 'intro_main.html', {'contents': contents, 'companys': companys})