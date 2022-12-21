from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    ss="<br/><br/><center><h2 style='color:red'>this is django first project</h2></center>"
    return HttpResponse(ss);
    
    
def show(req):
    print("wel/ url is req and executed");
    ss='''
<html>
	<head>
		<title>***Welcome to HTML***</title>
		<style>
		h1{
		color:red;
		}
		h2{
		color:black;
		}
		h3{
		color:blue;
		}
		h4{
		color:green;
		}
		h1,h3{
		bgcolor:yellow;
		}
		h2,h4{
		bgcolor:pink;}
	    </style>
	</head>
	<body>
		<center>
		<h1>this is html page</h1>
		<hr color=brown width=70%/>
		<h2>this is html page</h2>
		<hr color=violet width=80%/>
		<h3>this is my first page</h3>
		<hr color=darkgreen width=90%/>
		<h4>this is my first page</h4>
		<hr color=black width=100%/>
		</center>
	</body>
</html>
		
'''
    return HttpResponse(ss);

def f1(req):
    return HttpResponse("calls f1 function form FirstApp");
    
def f2(req):
    return HttpResponse("calls f2 Func From First App");

#git function
def git_view_func(request):
	return HttpResponse("<h1> Hello from git hub view function</h1><hr/>");



