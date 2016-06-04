from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Company, Author, Content, CompanyImage
# Create your views here.

def index(request):
    img = CompanyImage.objects.all()
    lists = Content.objects.order_by('-created_date')
    pagenator = Paginator(lists, 5)
    page = request.GET.get('page')
    try:
        company_contents = pagenator.page(page)
    except PageNotAnInteger:
        company_contents = pagenator.page(1)
    except EmptyPage:
        company_contents = paginator.page(pagenator.num_pages)
    return render(request, 'index.html', {'img': img, 'company_contents': company_contents})

def main_list(request, companyid):
    companys = Company.objects.all()
    contents = Content.objects.filter(company_name = companyid)
    paginator = Paginator(contents, 10)
    page = request.GET.get('page')
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    return render(request, 'company/main_list.html', {'companys': companys, 'lists': lists})

def content_list(request, company_name_pk):
    content = Content.objects.filter(company_name_pk)

def main_detail(request, pk):
    content = get_object_or_404(Content, pk = pk)
    return render(request, 'company/main_detail.html', {'content': content})
