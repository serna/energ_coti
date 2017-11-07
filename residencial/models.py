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
		verbose_name_plural = "Tarifas" 

class Comercial(models.Model):
	costo_1er_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_2do_escalon = models.DecimalField(max_digits = 7,decimal_places=3)
	costo_excedente = models.DecimalField(max_digits = 7,decimal_places=3)
	rango_1er_escalon = models.IntegerField()
	rango_2do_escalon = models.IntegerField()
	cargo_fijo = models.DecimalField(max_digits = 7,decimal_places=3)

class Inversor(models.Model):
	nombre = models.CharField(max_length=20)
	potencia_pico = models.DecimalField(max_digits = 4,decimal_places=2)
	costo = models.DecimalField(max_digits = 8,decimal_places=2)
	costo_de_instalacion = models.DecimalField(max_digits = 8,decimal_places=2)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Inversores"
	def __str__(self):
		return str(self.nombre) 
class Proovedor(models.Model):
	nombre_proovedor = models.CharField(max_length=20)
	contacto = models.CharField(max_length=50)
	panel = models.DecimalField(max_digits = 7,decimal_places=2)
	conector_hembra_APS = models.DecimalField(max_digits = 7,decimal_places=2)
	protective_end_cap = models.DecimalField(max_digits = 7,decimal_places=2)
	midClamp = models.DecimalField(max_digits = 7,decimal_places=2)
	endClamp = models.DecimalField(max_digits = 7,decimal_places=2)
	base_triangular = models.DecimalField(max_digits = 7,decimal_places=2)
	metro_riel = models.DecimalField(max_digits = 7,decimal_places=2)
	cable = models.DecimalField(max_digits = 7,decimal_places=2)
	medidor = models.DecimalField(max_digits = 7,decimal_places=2)
	caja_registro = models.DecimalField(max_digits = 7,decimal_places=2)
	interruptor = models.DecimalField(max_digits = 7,decimal_places=2)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Proovedores"
	def __str__(self):
		return str(self.nombre_proovedor) + ', contacto: ' + str(self.contacto)
		
class Instalacion(models.Model):
	nombre = models.CharField(max_length=50)
	panel = models.DecimalField(max_digits = 7,decimal_places=2)
	conector_hembra_APS = models.DecimalField(max_digits = 7,decimal_places=2)
	protective_end_cap = models.DecimalField(max_digits = 7,decimal_places=2)
	midClamp = models.DecimalField(max_digits = 7,decimal_places=2)
	endClamp = models.DecimalField(max_digits = 7,decimal_places=2)
	base_triangular = models.DecimalField(max_digits = 7,decimal_places=2)
	metro_riel = models.DecimalField(max_digits = 7,decimal_places=2)
	cable = models.DecimalField(max_digits = 7,decimal_places=2)
	medidor = models.DecimalField(max_digits = 7,decimal_places=2)
	caja_registro = models.DecimalField(max_digits = 7,decimal_places=2)
	interruptor = models.DecimalField(max_digits = 7,decimal_places=2)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Costos de instalacion"
	def __str__(self):
		return str(self.nombre)
class Configuracion(models.Model):
	""" this model is used for thee economic configuration"""
	nombre = models.CharField(max_length=30)
	tipo_cambio = models.DecimalField(max_digits=4,decimal_places=2)
	utilidad = models.DecimalField(max_digits=3,decimal_places=2)
	indirectos = models.DecimalField(max_digits=3,decimal_places=2)
	IVA = models.DecimalField(max_digits=3,decimal_places=2)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Configuracion economica"
	def __str__(self):
		return str(self.nombre)
class Configuracion2(models.Model):
	nombre = models.CharField(max_length=30)
	potencia_panel = models.DecimalField(max_digits=4,decimal_places=0)
	longitud_del_string = models.DecimalField(max_digits=2,decimal_places=1) # Length of the string in meters	
	distancia_maxima_entre_triangulos = models.DecimalField(max_digits=2,decimal_places=1) # distance between triangles bases
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Configuracion fotovoltaica"
	def __str__(self):
		return str(self.nombre)