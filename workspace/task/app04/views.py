from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.



def ajax(request):
    if request.method == 'PORT':
        print request.POST
        return  HttpResponse('OK')
    else:
        return render_to_response('app04/ajax.html')
    
    
    