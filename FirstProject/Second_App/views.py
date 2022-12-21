from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime

# Create your views here.
def f11(req):
    ss=time.ctime();
    return HttpResponse(ss);
    
    
def f3(req):
    return HttpResponse("calls the f3 view function from SecondApp");
   
def f4(req):   
    return HttpResponse("calls the f4 view function from SecondApp");
   
def senddatetime(req):
    print("date & time is printed");
    ct=datetime.datetime.now();
    print("date and time is=",ct);
    ss='''
    <html>
        <head>
            <title>time & date</title>
            <style>
            h1{color:blue};
            h2{color:red};
            </style>
        </head>
        <body>
            <center>
                <h1>Welcome to Django</h1>
                <h2>''',ct,'''</h2>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(ss);