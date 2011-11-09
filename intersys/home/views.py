from django.shortcuts import render_to_response
from django.core.validators import email_re
from home.models import registros

# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
#    return render_to_response('home.html')

def index(request):
	resultado = 'Introduce tu e-mail'
	msg_mail = 'Introduce_tu_Email_aqui'
	if request.method == 'POST':
		email = request.POST.getlist('email')[0]
		if email_re.search(email):
			#checamos si existe el correo
			if len(registros.objects.filter(mail=email)) > 0:
				resultado = 'El correo ya se encuentra registrado'
			else:
				aux = registros(mail=email)
				aux.save()
				resultado = 'Gracias por registrarte'
		else:
			resultado = 'e-mail incorrecto'
		return render_to_response('home.html', {'resultado': resultado, 'msg_mail': msg_mail})
	else:
		print resultado, msg_mail
		return render_to_response('home.html', {'resultado': resultado, 'msg_mail': msg_mail})
