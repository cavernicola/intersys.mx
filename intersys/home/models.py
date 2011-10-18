from django.db import models

class registros(models.Model):
	mail = models.EmailField(help_text='Introduce tu Email', primary_key=True)
	
	def __unicode__(self):
		return self.mail
