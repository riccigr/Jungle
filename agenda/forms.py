#-*- coding utf-8 -*-

from django import forms
from django.forms import ModelForm
from agenda.models import ItemAgenda

class FormItemAgenda(forms.ModelForm):
	titulo = forms.CharField(max_length=100)
	data = forms.DateField(
		widget = forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%Y','%d%m%y'])
	hora = forms.TimeField()
	descricao = forms.CharField()
			
	class Meta:
		model = ItemAgenda
		fields = ('titulo', 'data', 'hora', 'descricao')