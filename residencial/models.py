from django.db import models

# Create your models here.
class Residencial(models.Model):
	tarifa = models.CharField(max_length=2)
	costo_basico = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_intermedio = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_excedente = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_DAC = models.DecimalField(max_digits = 7,decimal_places=3)
	rango_basico = models.IntegerField()
	rango_intermedio = models.IntegerField()
	rango_excedente = models.IntegerField()
	cargo_fijo = models.DecimalField(max_digits = 7,decimal_places=3)
	
	def __str__(self):
		return "Tarifa " + str(self.tarifa)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Servicio residencial" 

class Comercial(models.Model):
	costo_1er_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_2do_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_excedente = models.DecimalField(max_digits = 7,decimal_places=3)
	rango_1er_escalon = models.IntegerField()
	rango_2do_escalon = models.IntegerField()
	
	cargo_fijo = models.DecimalField(max_digits = 7,decimal_places=3)
	