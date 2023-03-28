from django import forms 
from django.db import models
from .models import QR

class transactionsForm(forms.ModelForm):
	contact = forms.IntegerField( 
		label='Enter Phone Number: ',
        required=True,
        widget=forms.TextInput(
				attrs={
					'class':'form-control',	
					'placeholder':'254...',			 
				}
			)
		)
	# 
	amount = forms.IntegerField(required=True,widget=forms.HiddenInput(
		attrs={
			'class':'form-control',	
			 'value': 1, 
		}))
		# code field form
	code = forms.ImageField(required=False,widget=forms.HiddenInput())
	class Meta:
		model = QR
		fields = ['contact']