from django.contrib import admin
from django.utils import timezone
from .models import Company, Author, Content
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('tag', 'tagline')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'company_name', 'created_date', 'pub_date')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Content, ContentAdmin)
