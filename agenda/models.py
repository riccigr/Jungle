from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	usuario = models.ForeignKey(User, related_name='item_usuario')
	participantes = models.ManyToManyField(User, related_name='item_participantes')
'''
def envia_email(**kwargs):
	print "Essa function enviara emails, aguarde..."
	try:
		item = kwargs['instance']
	except KeyError:
		print "ops"
		return
	for part in item.participantes.all():
		print "tem paricipantes"
		if part.email:
			print "aki foi"
			dados = (item.titulo, 
					datetime.strftime(item.data, "%d/%m/%Y"), 
					item.hora)
			part.email_user(subject = "[evento] %s dia %s as %s" % dados,
			 				message = "Evento: %s \nDia: %s \nHora: %s" % dados,
							from_email = item.usuario.email)	
	
models.signals.post_save.connect(envia_email, sender=ItemAgenda, dispatch_uid="agenda.models.ItemAgenda")
'''
