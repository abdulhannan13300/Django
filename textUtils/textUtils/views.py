# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Abdul Hannan', 'place':'Mumbai'}
    return render(request, 'index.html',params)

def about(request):
    a = '''
    <h1>About Page<h1> 
    <a href="https://mail.google.com/mail/"> Gmail</a>
    <a href="/">Back To Home Page</a>
    '''
    return HttpResponse(a)

def analyze(request):
    
    
    data = request.POST.get('inputText','default')
    
    removepunc = request.POST.get('remPunc','off')
    charcount = request.POST.get('charCount','off')
    newlineremover = request.POST.get('newLineRem','off')
    fullcaps = request.POST.get('fullCaps','off')
    extraspaceremover = request.POST.get('extraSpaceRem','off')
    
    print(data)
    
    if (removepunc != 'on' and fullcaps !='on' and extraspaceremover !="on" 
        and newlineremover != "on" and charcount != "on"):
        return HttpResponse("Please select an appropriate options")
    
    if removepunc == 'on':
        analyzed = ''
        for char in data:
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)        
    
    if(fullcaps=='on'):
        analyzed = ""
        for char in data:
            analyzed += char.upper()
        params = {'purpose':'Change to Upppercase', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)        
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(data):
            if not(data[index] == " " and data[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)        

    if (newlineremover == "on"):
        analyzed = ""
        for char in data:
            #charage return returna new line with \r
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
        
    if(charcount=='on'):
        count = 0
        for char in data:
            count += 1
        print("From"+data)
        params = {'purpose':'Character Counter', 'analyzed_text':count}
        return render(request,'analyze.html',params)    
                 
     
    