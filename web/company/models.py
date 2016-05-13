from django.db import models
from django.utils import timezone
# Create your models here.
#
class Company(models.Model):
    tag = models.CharField(max_length = 200)
    tagline = models.TextField()
    def __str__(self):
        return self.tag

class Author(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Content(models.Model):
    company_name = models.ForeignKey(Company)
    headline = models.CharField(max_length = 255)
    body_text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    pub_date = models.DateTimeField(blank = True, null = True)
    authors = models.ManyToManyField(Author)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline
