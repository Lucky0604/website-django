from django.shortcuts import render
from django.utils import timezone
from .models import Culture, CultureContent
# Create your views here.
def culture_list(request, cultureid):
    culture_list = Culture.objects.all()
    culture_detail = CultureContent.objects.filter(culture_name = cultureid)
    context = {'culture_list': culture_list, 'culture_detail': culture_detail}
    return render(request, 'culture_list.html', context)
