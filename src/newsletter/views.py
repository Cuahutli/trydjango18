from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.conf import settings

from .forms import SignUpForm, ContactForm

from .models import SignUp
from django.contrib.auth.models import User




# Create your views here.
def home(request):
	title = "Recibe nuevas noticias"
	form = SignUpForm(request.POST or None)
	# if request.user.is_authenticated():
	# 	title = "Mi titulo %s" % (request.user)
	

	context = {
		"title": title,
		"abc": 123,
		"form" : form
	}

	if form.is_valid():
		# form.save()
		#print(request.POST['email']) #not recomended
		instance = form.save(commit=False)
		if not instance.fullname:
			instance.fullname= "Yepale"
		instance.save()
		context = {
			"title": "Gracias"

		}
	if request.user.is_authenticated() :#and request.user.is_staff:
		es_grupo = "sin grupo"
		grupos = request.user.groups.all()
		print(grupos)
		for grupo in grupos:
			if grupo.name in ('recordatorios'):
				es_grupo = "con grupo"
				
		 # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
		# i = 1
		# for instance in  SignUp.objects.all():
		# 	print (i,instance.fullname)
		# 	i += 1
		# queryset = SignUp.objects.all().order_by('-timestamp').filter(fullname__iexact="cuahutli")
		queryset = SignUp.objects.all().order_by('-timestamp')
		#print (SignUp.objects.all().order_by('-timestamp').filter(fullname__iexact="cuahutli").count())
		context = {
			"queryset": queryset,
			"es_grupo": es_grupo
		}
	print(context)
	return render(request,"home.html", context)

def contact(request):
	title = 'Contacto'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print (key, form.cleaned_data.get(key))	
		# for key, value in form.cleaned_data.iteritems():
		# 	print (key, value)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_fullname = form.cleaned_data.get("fullname")

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]#,'lyalepa@gmail.com']
		contact_message = """
			%s: %s via %s
		""" %(form_fullname, form_message, form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=False )

	context = {
		"form": form,
		"title": title,
	}
	return render(request,"forms.html", context)