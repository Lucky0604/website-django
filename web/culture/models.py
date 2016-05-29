from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from company.models import Author
# Create your models here.

class Culture(models.Model):
    cultureid = models.IntegerField(primary_key = True, unique = True)
    culture_item = models.CharField(max_length = 200)
    culture_tag = models.CharField(max_length = 200)

    class Meta:
        verbose_name = 'Culture'
        verbose_name_plural = 'Culture'

    def __str__(self):
        return self.culture_tag

class CultureContent(models.Model):
    culture_name = models.ForeignKey(Culture, to_field = 'cultureid', db_column = 'culture_name')
    culture_headline = models.CharField(max_length = 200)
    culture_bodytext = HTMLField()
    created_date = models.DateTimeField(default = timezone.now)
    pub_date = models.DateTimeField(blank = True, null = True)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Culture Content'
        verbose_name_plural = 'Culture Content'

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.culture_headline
