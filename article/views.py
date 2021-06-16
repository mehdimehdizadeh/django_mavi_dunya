from django.core import paginator
import article
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404,reverse
from .models import Article,Category,About,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def category(request,id):
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":article})
    cate = Category.objects.filter(id = id).first()
    category = Category.objects.all()
    posts_list = Article.objects.filter(category=cate)
    paginator = Paginator(posts_list,20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
        "categories":category,
    }
    return render(request,"category.html",context)


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list,20)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles =paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":article})
    
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "articles":articles,
    }
    return render(request,"index.html",context)

def about(request):
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":article})
    categories = Category.objects.all()
    about = About.objects.all()[:1]
    context = {
        "categories":categories,
        "about":about,
    }
    return render(request,"about.html",context)

def detail(request,id):
    keyword = request.GET.get("keyword")
    if keyword:
        article = Article.objects.filter(title__contains = keyword)
        return render(request,"index.html",{"articles":article})
    categories = Category.objects.all()
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id = id)
    comment = article.comments.all()
    context = {
        "categories":categories,
        "article":article,
        "comments":comment,
    }
    return render(request,"detail.html",context)

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_content = request.POST.get("comment_content")
        comment_name = request.POST.get("name")

        newComment = Comment(comment_content = comment_content,comment_name=comment_name)

        newComment.article = article

        newComment.save()

    return redirect("/articles/article/"+str(id))

