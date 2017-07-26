from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm, servicio_residencial_form
import rutinas as rut
# Create your views here.

def prom_anual_kwhr(request):
	if request.method == 'POST':
		form = servicio_residencial_form(request.POST)
		if form.is_valid():
			b1 = form.cleaned_data['consumo_1er_bimestre']
			b2 = form.cleaned_data['consumo_2do_bimestre']
			b3 = form.cleaned_data['consumo_3er_bimestre']
			b4 = form.cleaned_data['consumo_4to_bimestre']
			b5 = form.cleaned_data['consumo_5to_bimestre']
			b6 = form.cleaned_data['consumo_6to_bimestre']
			promedio = (b1+b2+b3+b4+b5+b6)/6.0
			print("El promedio anual es de ",promedio)
			context = {	"titulo": "El promedio de consumo bimestral es de " + str(round(promedio,2))+" kWh",
						'lista':rut.calculaResidencial(promedio),
						}
			lista = [1,2,3,4,5,6,7,8,9]
			return render(request,"cotizacion_residencial.html", context)
	else:
		form = servicio_residencial_form()

	context = {
		"mensaje": "nada",
		"form":form,
	}
	return render(request, "prom_anual_kwhr.html", context)
def start_page(request):
	context = {
		"instance": "nada",
	}
	return render(request, "base.html", {})
def domestico(request):
	context = {
		"instance": "nada",
	}
	return render(request, "residencial.html", context)
def get_name(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		print "We are about to check validity"
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			print "La validacion fue exitosa y correcta"
			context = {"mensaje":"Hemos capturado tu nombre correctamente",
						"nombre": form.cleaned_data['your_name']}
			return render(request, 'mensaje.html',context)
		else:
			print "La validacion fue exitosa e incorrecta"

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})