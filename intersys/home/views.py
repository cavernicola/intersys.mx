from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render_to_response('home.html')

  
def suscribir(request):
	if request.is_ajax():
		#return render_to_response('home.html',{'resultado': 'hola'})
		return HttpResponse('hola')