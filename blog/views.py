from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
    print('I am home view')
    return HttpResponse('This is Home page')

def excep(request):
    print('I am Excep view')
    a = 10/0
    return HttpResponse('This is Excep page')



def user(request):
    print('I am User Info view')
    context = {'name':'Rahul'}
    return TemplateResponse(request, 'blog/user.html',context)

