from django import forms
from .models import Residencial
class NameForm(forms.Form):
	BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
	opciones_mes = (
			('ENERO','ENERO'),
			('FEBRERO','FEBRERO'),
			('MARZO','MARZO'),
			('ABRIL','ABRIL'),
			('MAYO','MAYO'),
			('JUNIO','JUNIO'),
			('JULIO','JULIO'),
			('AGOSTO','AGOSTO'),
			('SEPTIEMBRE','SEPTIEMBRE'),
			('OCTUBRE','OCTUBRE'),
			('NOVIEMBRE','NOVEIMBRE'),
			('DICIEMBRE','DICIEMBRE'),
	)

	your_name = forms.MultipleChoiceField(
		required=False,
		#widget=forms.CheckboxSelectMultiple,
		choices= opciones_mes,
	)
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

class servicio_residencial_form(forms.Form):
	tarifa = forms.ModelChoiceField(queryset=Residencial.objects.all())
	consumo_1er_bimestre = forms.IntegerField()
	consumo_2do_bimestre = forms.IntegerField()
	consumo_3er_bimestre = forms.IntegerField()
	consumo_4to_bimestre = forms.IntegerField()
	consumo_5to_bimestre = forms.IntegerField()
	consumo_6to_bimestre = forms.IntegerField()
	