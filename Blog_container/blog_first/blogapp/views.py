from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from .models import Blog
from django.contrib.auth.decorators import login_required

from blogapp.models import Blog
from django.db.models import Q


# Create your views here.
# def home(request):
#     return HttpResponse('<h1>hello world</h1>')

# def home(request):
#     return render(request,'blogapp/home.html')

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')

def home(request):
    posts = Blog.objects.all().filter(activeYN=1).order_by('-modifiedAt')
    print(posts)
    context={
        'keyposts':posts
    }

    return render(request,'blogapp/home.html',context)

def create(request):
    return render(request,'blogapp/form.html')

@login_required
def profile(request):
    return render(request,'blogapp/profile.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    blog = Blog(title=title, content=content)
    blog.save()
    return redirect('/blog/home')

def edit(request,pk):
    posts = Blog.objects.all().filter(Q(id=pk) & Q(activeYN=1)).first()
    context={
        'keyposts':posts #post[0] because we need only the dictionary and not list of dictionary
    }

    # print(result)
    # print(pk)
    print(context)
    return render(request,'blogapp/editForm.html',context)

def update(request):
    id=request.POST['id']
    title=request.POST['blogTitle']
    content=request.POST['content']
    blog = Blog.objects.get(id=id)
    blog.title = title
    blog.content = content
    blog.save()
    return redirect('/blog/home')


def delete(request,pk):
    blog = Blog.objects.get(id=pk)
    blog.activeYN = 0
    blog.save()
    return redirect('/blog/home')
