from django.db import models
from django.utils import timezone
# Create your models here.



class Company(models.Model):
    companyid = models.IntegerField(primary_key=True, unique=True)
    company_name = models.CharField(max_length = 200)
    tagline = models.TextField()

    class Meta:
        verbose_name = '公司名称'
        verbose_name_plural = '公司名称'

    def __str__(self):
        return self.company_name

class Author(models.Model):
    author_name = models.CharField(max_length = 50)
    email = models.EmailField()

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):
        return self.author_name

class Content(models.Model):
    company_name = models.ForeignKey(Company, to_field='companyid', db_column='company_name')
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    pub_date = models.DateTimeField(blank = True, null = True)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline

class CompanyImage(models.Model):
    image1 = models.ImageField(upload_to='company/')
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.headline
