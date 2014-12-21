#coding: utf-8
from core.models import Article
from core.models import Tag
from core.models import Category
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from util import pager

def getArticles(request,num=1):
    articles_all = Article.objects.all()
    p =  Paginator(articles_all,4)
    articles = p.page(int(num))
    tagList = Tag.objects.all()
    categoryList = Category.objects.all()
    page = pager.Pager(pageNumber=num, total=len(articles_all), limit=4)
#     print page.navigatePageNumbers
    print page.hasPreviousPage
    return render_to_response('list.html',{'articles':articles,'tags':tagList,'categories':categoryList,'request':request,'islistView':True,'pager':page})
    
def getArticlesBySlug(request,slug):
    article = Article.objects.get(slug=slug)
    tagList = Tag.objects.all()
    categoryList = Category.objects.all()
    return render_to_response('article.html',{'article':article,'tags':tagList,'categories':categoryList,'islistView':False})
    
def getArticlesByTag(request,tag):
    articleList = Article.objects.get(tag=tag)
    tagList = Tag.objects.all()
    categoryList = Category.objects.all()
    return render_to_response('list.html',{'articles':articleList,'tags':tagList,'categories':categoryList})

def getArticlesByCategory(request,category):
    articleList = Article.objects.get(category=category)
    tagList = Tag.objects.all()
    categoryList = Category.objects.all()
    return render_to_response('list.html',{'articles':articleList,'tags':tagList,'categories':categoryList})

def page(request,paginator,num):
    if paginator.count < 6:
        pageList = [1,2,3,4,5]
        return pageList
        
    

def test(request):
    a = "1";
    print a;
    return render_to_response('111.html',a)