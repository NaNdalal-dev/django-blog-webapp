from django.shortcuts import render
from .models import Blog
def home(request):
	blogs = Blog.objects.all()[::-1]
	return render(request,"home.html",{'blogs':blogs})

def blog_in_detail(request, link):
	blog =  Blog.objects.get(id=link)
	blg_field = blog.BlogField.split('\n')
	return render(request,"blog.html",{'blog':blog,'blg_field':blg_field,'title':blog.Title})
