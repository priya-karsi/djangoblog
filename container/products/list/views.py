from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    cursor=connection.cursor()
    cursor.execute('SELECT name,summary,color,size,price,buy,cname FROM products_table NATURAL JOIN category where cId=1;')

    columns=[col[0] for col in cursor.description]
    products_info=[
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]
    print(products_info)

    context={
        'keyproducts':products_info
    }

    # return HttpResponse('<h1>Welcome to home</h1>')
    return render(request,'list/home.html',context)