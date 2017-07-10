from django.db import models

# Create your models here.
class Tarifa(models.Model):
	anio = models.CharField(max_length=10)
	mes = models.CharField(max_length=10)
	residencial_basico = models.DecimalField(max_digits = 7,decimal_places=3)
	residencial_intermedio = models.DecimalField(max_digits = 7,decimal_places=3)
	residencial_excedente = models.DecimalField(max_digits = 7,decimal_places=3)
	DAC = models.DecimalField(max_digits = 7,decimal_places=3)
	residencial_cargo_fijo = models.DecimalField(max_digits = 7,decimal_places=3)
	comercial_1er_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	comercial_2do_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	comercial_excedente = models.DecimalField(max_digits = 7,decimal_places=3)
	comercial_cargo_fijo = models.DecimalField(max_digits = 7,decimal_places=3)
	def __str__(self):
		return self.mes + "-" + self.anio