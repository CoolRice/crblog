#coding: utf-8
from django.db import models
from django.utils import timezone

from crblog.managers import DRAFT, HIDDEN, PUBLISHED

class Category(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50,unique=True)
    
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return 
    
class Tag(models.Model):
    name = models.CharField(max_length = 10)
    slug = models.CharField(max_length = 10,unique=True)
    
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return
    
class Article(models.Model):
    
    STATUS_CHOICES = ((DRAFT, 'draft'),
                      (HIDDEN, 'hidden'),
                      (PUBLISHED, 'published'))
    
    type = models.CharField(max_length = 10)                        #类型原，译，转
    
    title = models.CharField(max_length = 50)
    
    slug = models.SlugField(max_length = 50,unique=True)
    
    content = models.TextField()
    
    date = models.DateTimeField(auto_now=True)
    
    clickCount = models.IntegerField()
    
    category = models.ForeignKey(Category)
    
    tags = models.ManyToManyField(Tag,blank=True)
    
    status = models.IntegerField(db_index=True,choices=STATUS_CHOICES, default=DRAFT)
    
    start_publication = models.DateTimeField(blank=True, null=True)
    
    last_update = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-date']
    
    def __unicode__(self):
        return "title"+self.title
    
    def is_visible(self):
        return 
    def previous_post(self):
        return
    
    def next_post(self):
        return
    
    def short_url(self):
        return
    
    def get_absolute_url(self):
        
        return "1111"
    
class LinkExchange(models.Model):
    name = models.CharField(max_length = 50)
    url = models.CharField(max_length = 50,unique=True)
    
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return
    