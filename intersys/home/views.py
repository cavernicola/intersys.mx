from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render_to_response('home.html')

@csrf_protect
def suscribir(request):
	if request.POST:
		print "post"
		return render_to_response('home.html')
	else:
		return render_to_response('home.html')
