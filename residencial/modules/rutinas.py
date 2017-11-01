# Her are the definition of all tha functions that would be doing the maths
import numpy as np

from residencial.models import Residencial, Configuracion2,Inversor
from math import ceil, floor
def lista():
	return ["Cesar","Oscar"]

def inversion(nCells):
	""" Return the instalation cost of nCells
		
		nCells [int]: The number of cells 
		
		This function returns the cost of instalation of nCells, it takes into consideration that cost do not behaves linearly with the 
		number of cells, the rules to define the cost of instalation are:
		
		1.- Instalation cost: 1-8 cells is $4000.00, 9-16 $8000,00 and so on
		2.- Each cell cost: $7,200.00
		3.- Protection circuit: $5,00.00
		4.- Saler commission: 10%.
		5.- Administration commission: $1,620.00 the very first cell then $720.00 each extra cell
		6.- Utility: 20%
	"""
	if nCells == 0:
		return 0,0,0,0,0,0,0,0
	instCost = 4000*((nCells-1)/8+1)
	cellsCost = 7200*nCells
	protectionCircuitCost = 5000
	partial = instCost + (cellsCost + protectionCircuitCost)
	salerComm = partial*0.1
	admCost = partial*0.1
	totalCost = partial + salerComm + admCost
	utility = 0.2*partial
	totalCost = partial + salerComm + admCost + utility
	return totalCost,instCost,cellsCost, protectionCircuitCost, partial, salerComm, admCost, utility

def noCeldasRes(consumo):
	""" This function returns the maximum number of needed cells 
		
		consumption [int]: The bimestral consumption of the client
		
		This function returns the maximum number of cells needed to supply the total energy demand based on the bimestral consumption,
	"""
	return consumo/75.0
	
def pagoCFE(consumption,tarifa):
	""" Computes the charge done to the user according to CFE rates
	    powerDemand [int]: the power used bimonthly by the user
	"""
	obj = Residencial.objects.filter(id=tarifa)
	#print('la tarifa es ',obj,tarifa)
	#print("TARIFA: " + str(tarifa))
	#print("MENSAJE: " + str(obj) + " " + str(tarifa) + " " + str(type(tarifa))) 
	basicCost = float(obj[0].costo_basico)
	middleCost = float(obj[0].costo_intermedio)
	excessCost = float(obj[0].costo_excedente)
	DACcost = float(obj[0].costo_DAC)
	rango_DAC = float(obj[0].rango_excedente)
	rango1 = float(obj[0].rango_basico)
	rango2 = float(obj[0].rango_intermedio)-rango1


	iva = 0.16
	powerDemand = consumption
	if powerDemand>rango_DAC:
 		pagoFijo = float(obj[0].cargo_fijo)
 		total = pagoFijo + powerDemand*DACcost
 		#return pagoFijo + powerDemand*DACcost
	else:
		if powerDemand>rango1: # when user is in in middle consumption
			total = rango1*basicCost # full first step
			consumption -= rango1 # just take into account from  middle to excess step
			if consumption>rango2: #if consmumption is on the third step
				total+= rango2*middleCost
				consumption -= rango2
				total += consumption*excessCost
			else:
				total += consumption*middleCost
			#return total
		else:
			total = consumption*basicCost # When user is in basic consumption
			#return total
	return total*(1.0+iva)

def pagoCFEComercial(consumption):
	""" Computes the charge done to the user according to CFE rates, comercial fees
	    powerDemand [int]: the power used bimonthly by the user
	"""

	basicCost = 2.780
	middleCost = 3.356
	excessCost = 3.699
	iva = 0.16
	pagoFijo =  	65.93
	#	print("El consumo recibido es: ",consumption)
	#print("El consumo recibido es:",consumption)
	total = pagoFijo + consumption*basicCost # When user is in basic consumptio 
	if consumption>100:
		total = pagoFijo+100*basicCost # full first step
		consumption -= 100 # just take into account from  middle to excess step
		if consumption>100: #if consmumption is on the third step
			total+= 100*middleCost
			consumption -= 100
			if consumption>0:
				total+= consumption*excessCost
		else:
			total += consumption*middleCost
	#print(consumption,total)
	return total*(1.0+iva)
def fillWithZeros(a,size):
	""" This function fill with zeros a number

		a [int]: number to convert in string of size digits
		size [int]: the number of digits the number-string will be
		Example: if a = 15 and size = 4 the output will be 0015
		Example: if a = 150 and size = 5 the output will be 00150
	"""
	ans = '0'
	for i in range(size):
		if len(str(a))<size-i:
			ans += "0"
		else:
			break
	ans += str(a)
	return ans
def calculaResidencial(consumo,tarifa):
	entry = Configuracion2.objects.get(pk=1)
	#print("La tarifa es: " ,entry)
	sunHours = 5
	energyReduction = float(entry.potencia_panel)/1000.0*sunHours*(365/6)
	consumo = int(consumo)
	pagoActual = pagoCFE(consumo,tarifa)
	pagoAnterior = pagoActual
	#print "nCell\tpagoCFE \tInvers\tAhorro\tROI"
	nCells = 0 
	datos = []
	while consumo>0:
		ahorro = pagoActual-pagoCFE(consumo,tarifa)
		inver = inversion(nCells)[0]
		pago = pagoCFE(consumo,tarifa)
		print ("LA salida es ",fillWithZeros(nCells,4))
		if ahorro != 0:
			datos.append([fillWithZeros(nCells,4),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),str(round((inver/ahorro)/6.0,2)),str(round(pagoAnterior-pago,2))])
		else:
			datos.append([fillWithZeros(nCells,4),str(round(pago,2)),str(round(inver,2)),str(round(ahorro,2)),"No hay ROI" ,str(round(pagoAnterior-pago,2))])
		pagoAnterior = pago
		nCells += 1
		consumo -= energyReduction
	return datos
def calculaResidencial2(consumo,tarifa):
	entry = Configuracion2.objects.get(pk=1)
	#print("La tarifa es: " ,entry)
	sunHours = 5
	energyReduction = float(entry.potencia_panel)/1000.0*sunHours*(365/6)
	consumo = int(consumo)
	pagoActual = pagoCFE(consumo,tarifa)
	pagoAnterior = pagoActual
	#print "nCell\tpagoCFE \tInvers\tAhorro\tROI"
	nCells = 0 
	datos = []
	while consumo>0:
		ahorro = pagoActual-pagoCFE(consumo,tarifa)
		inver = inversion(nCells)[0]
		pago = pagoCFE(consumo,tarifa)
		print ("LA salida es ",fillWithZeros(nCells,4))
		if ahorro != 0:
			datos.append([fillWithZeros(nCells,4),str(round(pago,2)),str(round(ahorro,2))])
		else:
			datos.append([fillWithZeros(nCells,4),str(round(pago,2)),str(round(ahorro,2))])
		pagoAnterior = pago
		nCells += 1
		consumo -= energyReduction
	return datos
def numEndClamps(nModules,nModulesPerArray):
    """ Return the number of end clapms
    
        nPaneles [int]: The mumber photovoltaic modules
        nPanelesPorArreglo: The size of each string of modules.
    """
    # here an array is a set of n modules, where n is defined by user
    
    nArrays = int(nModules/nModulesPerArray)

    if nModules%nModulesPerArray:
        nArrays += 1
    return nArrays*4 # the factor 4 is because there are 4 end clamps for each array
def numMidClamps(nModules,nModulesPerArray):
    """ Return the number of mid clapms
    
        nPaneles [int]: The mumber photovoltaic modules
        nPanelesPorArreglo: The size of each string of modules.
    """
    # here an array is a set of n modules, where n is defined by user
    nArrays = numEndClamps(nModules,nModulesPerArray)/4
    res = nModules%nModulesPerArray
    nMidClamps = (nArrays)*(nModulesPerArray-1)
    if res:
        nMidClamps -= nModulesPerArray-nModules%nModulesPerArray
    return int(nMidClamps*2)
def trianglesPerString(stringLenght,maxDistanceAmong):
    """ Return the number of triangular bases needed given the maximum distance between bases and the lenght of the string
    
        stringLenght [float]: The length of the string in modules,it est, how many mocules are between each triangular base
        maxDistanceAmong [float]: The maximum distance among each triangular base in modules
    """
    if stringLenght ==0:
        return 0
    #compute how many times maxDistanceAmong fit into thje stringlenght
    nPerString = float(stringLenght)/float(maxDistanceAmong) # the amount of triangular bases per string
    #if it is not an integer number, then maybe ut is necessary to put an extra triangle
    if nPerString-int(nPerString)>0.1:
        nPerString=int(nPerString)+2 # it is necessary to add an extra triangle base
    else:
        nPerString=int(nPerString)+1 # it is possible to extend a little bit the ditance among triangles
    return int(nPerString)
def nTriangles(nModules):
    """ Return the number of thriangles needed for instalation
        
        nString [int]: The number of total strings
        stringLenght [float]: The length of the string in modules,it est, how many mocules are between each triangular base
        maxDistanceAmong [float]: The maximum distance among each triangular base in modules
    """
    # compute the number of triangles per string 
    entry = Configuracion2.objects.get(pk=1)
    stringLenght = float(entry.longitud_del_string)
    maxDistanceAmong = entry.distancia_maxima_entre_triangulos
    nPerString = trianglesPerString(stringLenght,maxDistanceAmong)
    nStrings = int(float(nModules)/stringLenght)
    missingModules = nModules-stringLenght*nStrings # the number of modules that doesn not fit in a complete sting
    nMissingTriangles = trianglesPerString(missingModules,maxDistanceAmong)
    return nPerString*nStrings+nMissingTriangles
def nMeters(nModules):
    """ Returns the number of meters of rail needed for instalation
        
        nModules [int]: Number of photovoltaic modules
    """
    return nModules*2

#invertersDict = {'micro0.5':[175.9,0.62],
#                'micro1.0':[303.2,1.24],
#                'play2.5':[866.8,3.33],
#                'play2.7':[912,3.60],
#                'play3.0':[884,4.0],
#                'play3.3':[965.5,4.4],
#                'play3.6':[982.6,4.80],
#                'play4.6':[1051.3,6.0],
#                'play5.5':[1336.3,7.33],
#                'play6':[1308.6,7],
#                'play10tl':[2400.70,13.33],
#                'play15tl':[2631.5,20],
#                'play20tl':[2987.8,26.67]}


def buildInvertersDict():
	entry = Inversor.objects.all()
	invertersDict = {}
	for item in entry:
		invertersDict[item] = [item.costo,item.potencia_pico,item.costo_de_instalacion]
	print('Se ha creado el diccionario de inversores')
	return invertersDict
invertersDict = buildInvertersDict()
print("LOS INVERSORES SON",invertersDict)
def nInverters2(powerDemand,panelPower):
    """ Return a dictionary of the number of panels by interter
        
        powerDemand [float]: total power demand
        panelPower [float]: total photovoltaic module power
        invertersDict [dict]: dictionary with the available inverter models
    """
    # define the dictionary of inversors, the list element is [price,peak power]
    
    #print 'The number of panel by inverter is'
    newDict = {}
    panelPower = float(panelPower)
    #print(invertersDict)
    for key in invertersDict.keys():
        inverter = invertersDict[key]
        nPanels = floor(float(float(inverter[1])/(panelPower/1000)))
        #print(inverter,nPanels,panelPower)
        usdPerWatt = round(float(inverter[0])/nPanels/panelPower/1000,4)
        ### check if this key is not already taken into aacount ###
        for i in newDict.keys():
            if i==nPanels:
                nPanels += 0.01 # if two different inverter model has the panels capability 
        newDict[nPanels] = [key,usdPerWatt,invertersDict[key][0],invertersDict[key][2]] # this condition prevents of an error by the duplication
    
    return newDict

def generateSuma(nPanels,panelPower,nExtra):
    ''' returns the sumands which fit the power demand in panels
        
        nPanels [int]: the number of needed panels
        nExtra [int]: the number of extra panels to take into account to be empy in an inverter
    '''
    lista1 = nInverters2(nPanels,panelPower)
    #print lista
    lista = sorted(lista1.keys(),reverse=True)
    #print lista
    suma = 0
    index = 0
    print('La lista es ',lista,invertersDict)
    sumando = lista[index]
    ans = []
    costo = 0
    while suma<nPanels:
        sumaProv = suma + sumando
        #if sumaProv>nPanels+1:
        if sumaProv>nPanels+nExtra: #uncomment this line for more optimal result
            index += 1
            if index==len(lista):
                break
            sumando = lista[index]
            
        else:
            suma += sumando
            #print sumando,lista1[sumando]
            ans.append(lista1[sumando])
            costo += invertersDict[lista1[sumando][0]][0]
    return ans,costo
