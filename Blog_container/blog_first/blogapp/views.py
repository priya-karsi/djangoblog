from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from pymysql import *
from pymysql import cursors

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>hello world</h1>')

# def home(request):
#     return render(request,'blogapp/home.html')

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')

def home(request):
    cursor=connection.cursor()
    cursor.execute('select * from posts where softdelete=0')

    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    print(posts)

    context={
        'keyposts':posts
    }

    return render(request,'blogapp/home.html',context)
def create(request):
    return render(request,'blogapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor(cursor=cursors.DictCursor)
    cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from posts where softdelete = 0")
    return redirect('/blog/home')