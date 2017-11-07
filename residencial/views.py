from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm, servicio_residencial_form
from .modules import rutinas as rut
from .models import Proovedor, Instalacion, Configuracion, Configuracion2
#from reportlab.pdfgen import canvas

from decimal import Decimal
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
			tarifa = form.cleaned_data['tarifa']
			promedio = (b1+b2+b3+b4+b5+b6)/6.0
			print("El promedio anual es de ",promedio)
			print(tarifa.id)
			context = {	"titulo": "El promedio de consumo bimestral es de " + str(round(promedio,2))+" kWh",
						'lista':rut.calculaResidencial2(promedio,tarifa.id),
						}
			lista = [1,2,3,4,5,6,7,8,9]
			return render(request,"cotizacion_residencial.html", context)
	else:
		form = servicio_residencial_form()

	context = {
		"mensaje": "Llena los campos correspondientes",
		"form":form,
	}
	return render(request, "prom_anual_kwhr.html", context)
def start_page(request):
	context = {
		"instance": "nada",
	}
	return render(request, "base.html", {})
def domestico(request):
	#rut.buildInvertersDict()
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
		print("We are about to check validity")
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			print("La validacion fue exitosa y correcta")
			context = {"mensaje":"Hemos capturado tu nombre correctamente",
						"nombre": form.cleaned_data['your_name']}
			return render(request, 'mensaje.html',context)
		else:
			print("La validacion fue exitosa e incorrecta")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})
def cotizacion_nPaneles(request,nPaneles,ahorro,pagoCFE):
	# Defining the length of strings of phtotovoltaic modules
	rowLength = 4
	# Making th corresponding query
	entry = Proovedor.objects.get(pk=1)
	entry2 = Instalacion.objects.get(pk=1)
	entry3 = Configuracion.objects.get(pk=1)
	entry4 = Configuracion2.objects.get(pk=1)

	print(entry.panel)
	# Defining corresponding variables
	nPanels = int(nPaneles)
	emptySpaces = range(30) # the allowed empty panel spaces in inversors capacity
	ansDict1,costo1 = rut.generateSuma(nPanels,entry4.potencia_panel,emptySpaces[0])
	ansDict = ansDict1
	for i in emptySpaces[1:]:
		ansDict1,costo2 = rut.generateSuma(nPanels,entry4.potencia_panel,i)
		if costo2<costo1:
			costo1 = costo2
			ansDict = ansDict1
		
	nEndClamps = rut.numEndClamps(nPanels,rowLength)
	nAPSs = int(nEndClamps/4)# here assuming there is need one APS for each row
	nProtectEndCap = nAPSs # here assuming there is need one APS for each row
	nMidClamps = rut.numMidClamps(nPanels,rowLength)
	nTriangles = rut.nTriangles(nPanels)
	nRailMeters = rut.nMeters(nPanels)
	nMetersCable = 50
	medidorDig = 1
	cajaRegistro = 1
	interruptor = 1
	costoPanel =  entry.panel
	costoAPS = entry.conector_hembra_APS
	costoEndCap = entry.protective_end_cap
	costoMid = entry.midClamp
	costoEnd = entry.endClamp
	costoTriangle = entry.base_triangular
	costoRail = entry.metro_riel
	costoCable = entry.cable
	costoMedidor = entry.medidor
	costoCaja = entry.caja_registro
	costoInterruptor = entry.interruptor

	instPanel =  entry2.panel
	instAPS = entry2.conector_hembra_APS
	instEndCap = entry2.protective_end_cap
	instMid = entry2.midClamp
	instEnd = entry2.endClamp
	instTriangle = entry2.base_triangular
	instRail = entry2.metro_riel
	instCable = entry2.cable
	instMedidor = entry2.medidor
	instCaja = entry2.caja_registro
	instInterruptor = entry2.interruptor

	lista = [['Panel ',nPanels,costoPanel,nPanels*costoPanel,instPanel,nPanels*instPanel],\
		   ['Conector APS',nAPSs,costoAPS,nAPSs*costoAPS,instAPS,nAPSs*instAPS],\
		   ['Protective end cap',nProtectEndCap,costoEndCap,nProtectEndCap*costoEndCap,instEndCap,nProtectEndCap*instEndCap],\
		   ['Mid Clamps',nMidClamps,costoMid,nMidClamps*costoMid,instMid,nMidClamps*instMid],\
		   ['End Clamps',nEndClamps,costoEnd,nEndClamps*costoEnd,instEnd,nEndClamps*instEnd],\
		   ['Bases triangulares', nTriangles,costoTriangle,nTriangles*costoTriangle,instTriangle,nTriangles*instTriangle],\
		   ['Metros de riel',nRailMeters,costoRail,nRailMeters*costoRail,instRail,nRailMeters*instRail],\
		   ['Cable',nMetersCable,costoCable,nMetersCable*costoCable,instCable,nMetersCable*instCable],\
		   ['Medidor digital',medidorDig,costoMedidor,medidorDig*costoMedidor,instMedidor,medidorDig*instMedidor],\
		   ['Caja de registro',cajaRegistro,costoCaja,cajaRegistro*costoCaja,instCaja,cajaRegistro*instCaja],\
		   ['Interruptor',interruptor,costoInterruptor,interruptor*costoInterruptor,instInterruptor,interruptor*instInterruptor],\
		   ]
	for inverter in ansDict:
		lista.append([inverter[0],1,round(Decimal(inverter[2]),2),round(Decimal(inverter[2]),2),round(Decimal(inverter[3]),2),round(Decimal(inverter[3]),2)])
	subtotalProd = 0
	subtotalInst = 0
	for i in range(len(lista)):
		subtotalProd += lista[i][3]
		subtotalInst += lista[i][5]
	#subtotalProd = float(subtotalProd)
	#subtotalInst = float(subtotalInst)
	# add the row of subtotals
	util = entry3.utilidad
	indir = entry3.indirectos
	IVA = entry3.IVA
	
	row = ['Subtotal 1','','',subtotalProd,'',subtotalInst]
	lista.append(row)
	row = ['Utilidad','','',round(subtotalProd*util,2),'',round(subtotalInst*util,2)]
	lista.append(row)
	row = ['indirectos','','',round(subtotalProd*indir,2),'',round(subtotalInst*indir,2)]
	lista.append(row)
	totalProd = round(subtotalProd*(1+util+indir),2)
	totalInst = round(subtotalInst*(1+util+indir),2)

	row = ['Subtotal 2','','',totalProd,'',totalInst]
	lista.append(row)
		
	row = ['IVA','','',round(subtotalProd*(1+util+indir)*IVA,2),'',round(subtotalInst*(1+util+indir)*IVA,2)]
	lista.append(row)

	totalProd = round(subtotalProd*(1+util+indir)*(1+IVA),2)
	totalInst = round(subtotalInst*(1+util+indir)*(1+IVA),2)
	row = ['TOTAL','','',totalProd,'',totalInst]
	lista.append(row)
	

	ahorro = float(ahorro)
	print('el ahorro es de ',ahorro)
	lista2 = []
	TOTAL = totalProd+totalInst
	TOTAL = float(TOTAL)
	row = ['Inversion total (USD)',TOTAL]
	lista2.append(row)
	precioDolar = float(entry3.tipo_cambio)
	row = ['Retorno de inversion (años)',round(TOTAL*precioDolar/ahorro/6.0,2)]
	lista2.append(row)
	pagoCFE = float(pagoCFE)
	row = ['Pago bimestral a CFE (pesos)',pagoCFE]
	lista2.append(row)
	row = ['Precio por KW (USD)', round(TOTAL/(float(entry4.potencia_panel)*nPanels/1000),2)]
	lista2.append(row)

	context = {
		"titulo": "Detalle de cotizacion: " + str(nPanels) + " paneles.",
		'headersList' : ['Descripcion','Cantidad','PU','Subtotal material','Mano de obra','Subtotal mano de obra'],
		'lista' : lista,
		'titulo2': 'Detalle financiero',
		'headersList2' : ['Descripcion','Cantidad'],
		'lista2': lista2,
		

	}
	return render(request, "impresion.html", context)
def cotizacion_nPaneles2(request,nPaneles):
	# Defining the length of strings of phtotovoltaic modules
	rowLength = 4
	# Making th corresponding query
	entry = Proovedor.objects.get(pk=1)
	entry2 = Instalacion.objects.get(pk=1)
	entry3 = Configuracion.objects.get(pk=1)
	entry4 = Configuracion2.objects.get(pk=1)

	print(entry.panel)
	# Defining corresponding variables
	nPanels = int(nPaneles)
	emptySpaces = [0,1,30] # the allowed empty panel spaces in inversors capacity
	ansDict1,costo1 = rut.generateSuma(nPanels,entry4.potencia_panel,emptySpaces[0])
	ansDict = ansDict1
	for i in emptySpaces[1:]:
		ansDict1,costo2 = rut.generateSuma(nPanels,entry4.potencia_panel,i)
		if costo2<costo1:
			costo1 = costo2
			ansDict = ansDict1
		
	nEndClamps = rut.numEndClamps(nPanels,rowLength)
	nAPSs = int(nEndClamps/4)# here assuming there is need one APS for each row
	nProtectEndCap = nAPSs # here assuming there is need one APS for each row
	nMidClamps = rut.numMidClamps(nPanels,rowLength)
	nTriangles = rut.nTriangles(nPanels)
	nRailMeters = rut.nMeters(nPanels)
	nMetersCable = 50
	medidorDig = 1
	cajaRegistro = 1
	interruptor = 1
	costoPanel =  entry.panel
	costoAPS = entry.conector_hembra_APS
	costoEndCap = entry.protective_end_cap
	costoMid = entry.midClamp
	costoEnd = entry.endClamp
	costoTriangle = entry.base_triangular
	costoRail = entry.metro_riel
	costoCable = entry.cable
	costoMedidor = entry.medidor
	costoCaja = entry.caja_registro
	costoInterruptor = entry.interruptor

	instPanel =  entry2.panel
	instAPS = entry2.conector_hembra_APS
	instEndCap = entry2.protective_end_cap
	instMid = entry2.midClamp
	instEnd = entry2.endClamp
	instTriangle = entry2.base_triangular
	instRail = entry2.metro_riel
	instCable = entry2.cable
	instMedidor = entry2.medidor
	instCaja = entry2.caja_registro
	instInterruptor = entry2.interruptor

	lista = [['Panel ',nPanels,costoPanel,nPanels*costoPanel,instPanel,nPanels*instPanel],\
		   ['Conector APS',nAPSs,costoAPS,nAPSs*costoAPS,instAPS,nAPSs*instAPS],\
		   ['Protective end cap',nProtectEndCap,costoEndCap,nProtectEndCap*costoEndCap,instEndCap,nProtectEndCap*instEndCap],\
		   ['Mid Clamps',nMidClamps,costoMid,nMidClamps*costoMid,instMid,nMidClamps*instMid],\
		   ['End Clamps',nEndClamps,costoEnd,nEndClamps*costoEnd,instEnd,nEndClamps*instEnd],\
		   ['Bases triangulares', nTriangles,costoTriangle,nTriangles*costoTriangle,instTriangle,nTriangles*instTriangle],\
		   ['Metros de riel',nRailMeters,costoRail,nRailMeters*costoRail,instRail,nRailMeters*instRail],\
		   ['Cable',nMetersCable,costoCable,nMetersCable*costoCable,instCable,nMetersCable*instCable],\
		   ['Medidor digital',medidorDig,costoMedidor,medidorDig*costoMedidor,instMedidor,medidorDig*instMedidor],\
		   ['Caja de registro',cajaRegistro,costoCaja,cajaRegistro*costoCaja,instCaja,cajaRegistro*instCaja],\
		   ['Interruptor',interruptor,costoInterruptor,interruptor*costoInterruptor,instInterruptor,interruptor*instInterruptor],\
		   ]

	for inverter in ansDict:
		lista.append([inverter[0],1,round(Decimal(inverter[2]),2),round(Decimal(inverter[2]),2),round(Decimal(inverter[3]),2),round(Decimal(inverter[3]),2)])
	subtotalProd = 0
	subtotalInst = 0
	for i in range(len(lista)):
		subtotalProd += lista[i][3]
		subtotalInst += lista[i][5]
	#subtotalProd = float(subtotalProd)
	#subtotalInst = float(subtotalInst)
	# add the row of subtotals
	util = entry3.utilidad
	indir = entry3.indirectos
	IVA = entry3.IVA
	
	row = ['Subtotal','','',subtotalProd,'',subtotalInst]
	lista.append(row)
	row = ['Utilidad','','',round(subtotalProd*util,2),'',round(subtotalInst*util,2)]
	lista.append(row)
	row = ['indirectos','','',round(subtotalProd*indir,2),'',round(subtotalInst*indir,2)]
	lista.append(row)
	row = ['IVA','','',round(subtotalProd*(1+util+indir)*IVA,2),'',round(subtotalInst*(1+util+indir)*IVA,2)]
	lista.append(row)
	totalProd = round(subtotalProd*(1+util+indir)*(1+IVA),2)
	totalInst = round(subtotalInst*(1+util+indir)*(1+IVA),2)
	row = ['TOTAL','','',totalProd,'',totalInst]
	lista.append(row)
	
	listaFinal = [['Sistema fotovoltaico',
				round((subtotalProd+subtotalInst)*(1+util+indir),2),
				round((subtotalProd+subtotalInst)*(1+util+indir)*(IVA),2),
				round((subtotalProd+subtotalInst)*(1+util+indir)*(1+IVA),2)]]
	context = {
		"mensaje": "Cotizacion " + str(nPanels) + " paneles.",
		'headersList' : ['Descripcion','Subtotal', 'IVA','TOTAL'],

		'lista' : listaFinal
		

	}
	return render(request, "impresion.html", context)
