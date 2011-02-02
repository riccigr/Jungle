# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import ItemAgenda
from forms import FormItemAgenda

def index(request):
	return HttpResponse(u"Hello World")

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html", {'lista_itens': lista_itens })
	
def adiciona(request):
	if request.method == 'POST': #form enviado
		form = FormItemAgenda(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			item = ItemAgenda(data = dados['data'],
					hora = dados['hora'],
					titulo = dados['titulo'],
					descricao = dados['descricao'])
			item.save()
			return render_to_response('salvo.html',{})
	else: # via link - GET
		form = FormItemAgenda()
		return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

def item(request, nr_item):
	try:
		item = ItemAgenda.objects.get(pk=nr_item)
	except ItemAgenda.DoesNotExist:
		raise Http404()
	return render_to_response('item.html',{'item': item})
