#-*- encoding: utf8 -*-
from django import forms

from .models  import SignUp

class ContactForm(forms.Form):
	fullname 	= forms.CharField(required=False)
	email 		= forms.EmailField()
	message 	= forms.CharField()
	
	# def clean_email(self):
	# 	print(self.cleaned_data)
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split("@")
	# 	domain,extension = provider.split(".")
	# 	if not "edu" in extension:
	# 		raise forms.ValidationError("Por favor ingresa un correo con terminación .edu")
	# 	return email


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['fullname', 'email']
		### exclude = ['fullname']

	def clean_email(self):
		print(self.cleaned_data)
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain,extension = provider.split(".")
		if not "edu" in extension:
			raise forms.ValidationError("Por favor ingresa un correo con terminación .edu")
		return email

	def clean_fullname(self):
		fullname = self.cleaned_data.get('fullname')
		# if not "cuahutli" in fullname:
		# 	raise forms.ValidationError("tu nombre debe tener la cadena cuahutli")
		return fullname