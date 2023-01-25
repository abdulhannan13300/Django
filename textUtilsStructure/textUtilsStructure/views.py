# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    a ='''  
    <h1>Home<h1> 
    <a href="https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8"> Django Course </a><br>
    <a href="/about" >About</a><br>
    <a href="/remPunc">Remove Punctuation</a><br>
    <a href="/capFirst">Capitalize First Letter </a><br>
    <a href="/spaceRem">Space Remover </a><br>
    <a href="/charCount">Character Count </a><br>
    '''
    return HttpResponse(a)

def about(request):
    a = '''
    <h1>About Page<h1> 
    <a href="https://mail.google.com/mail/"> Gmail</a>
    <a href="/">Back To Home Page</a>
    '''
    # return HttpResponse('<a href="/home ">Back to Home Page</a>')
    return HttpResponse(a)
def remPunc(request):
    a = '''
    <h1>Remove Punctuation<h1> 
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)


def capFirst(request):
    a = '''
    <h1>Capitalize First Letter<h1> 
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)

def newLineRem(request):
    a = '''
    <h1>New Line Remover<h1> 
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)

def charCount(request):
    a = '''
    <h1>Character Count<h1> 
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)
    

def spaceRem(request):
    a = '''
    <h1>Space Remover<h1> 
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)
    