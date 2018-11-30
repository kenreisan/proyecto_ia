import datetime
from random import random, randrange, randint, choice

def main():
	
	tam_poblacion = int(input("\nIngrese el tamaño de la poblacion: "))
	tam_tablero = int(input("Ingrese el numero que quiere que tenga el puzzle: "))
	generaciones = int(input("Ingrese el numero de generaciones: "))
	conteo = 0
	aptitud_generacion = 0
	aux = 0
	mejor_generacion = 0

	archivo = open('datos.txt','w')

	poblacion = []
	nueva_gen = []

	print("\nY así iniciamos")
	poblacion = crear_poblacion(tam_poblacion,tam_tablero)

	for x in poblacion:
		print(str(x) + " " + str("Aptitud: ") + str(func_aptitud(x)))
	
	while (generaciones != 0):	#aqui se eligen a las parejas para el cruce

		conteo += 1
		aptitud_generacion = 0
		nueva_gen = vaciar_lista(nueva_gen)

		for i in range(0,tam_poblacion):
			#nueva_gen.append(seleccion(poblacion))
			nueva_gen.append(cruce(seleccion(poblacion),seleccion(poblacion)))

		dato0 = ("\nGeneracion " + str(conteo) + "\n")
		print(dato0)
		archivo.write(dato0)
		
		for lista_nueva_gen in nueva_gen:
			aptitud_generacion = aptitud_generacion + func_aptitud(lista_nueva_gen)
			dato = (str(lista_nueva_gen) + " Aptitud = " + str(func_aptitud(lista_nueva_gen)))
			print(dato)
			archivo.write(dato + "\n")

		dato2 = ("Aptitud de la Generacion " + str(conteo) + ": " + str(aptitud_generacion))
		print(dato2)
		archivo.write(dato2)

		if aptitud_generacion > aux:
			mejor_generacion = conteo
			aux = aptitud_generacion

		#copiar nueva_gen a poblacion
		for posicion in range(0,tam_poblacion):
			poblacion[posicion] = nueva_gen[posicion]

		generaciones -= 1

	print("\nLos datos fueron guardados en el archivo 'datos.txt'")

	dato1 = ("\nMejor Generacion: " + str(mejor_generacion))
	print(dato1)
	archivo.write(dato1)

'''
def elegir_padres(pool):

	padre = pool.pop(randint(0,len(pool)-1))
	madre = pool.pop(randint(0,len(pool)-1))

	cruce(padre,madre)'''


def crear_poblacion(medida, elementos):
	'''Población para el algoritmo genético.

	Recibe: <medida> int
			<elementos> int

	Devuelve:	lista de listas con numeros aleatorios
				sin repetir.

	Crea una lista que contiene listas con numeros desde el
	cero(0) hasta (<elementos> -1) acomodados aleatoriamente.
	El numero de listas que crea esta determinado por <medida>
	'''
	poblacion = []
	pool = []
	inicio = 0
	primer = 1

	for x in range(inicio,medida):
		pool = llenar_pool(elementos)
		poblacion.append([])
		for y in range(inicio,elementos):
			poblacion[x].append(pool.pop(randint(inicio,len(pool)-1)))

	return poblacion

def llenar_pool(magnitud):
	'''Lista de numeros para llenar a los individuos.

	Recibe:		<magnitud> int

	Devuelve: 	una lista con numeros desde el cero(0)
				hasta <magnitud>

	Es usada para llenar los individuos de la poblacion sin
	repetir numeros.
	'''

	pool = []
	for x in range(0,magnitud):
		pool.append(x)

	return pool

def func_aptitud(individuo):
	'''Calcula que tan apto es un individuo.

	Recibe:		<individuo> lista

	Devuelve:	Entero que indica la aptitud

	Revisa los elementos de los individuos y si estan
	en su posicion correspondiente aumenta el valor de
	la aptitud.
	'''

	aptitud = 0

	for x in range(0,len(individuo)):
		#print(str(x) + " = " + str(individuo[x]))
		if individuo[x] == x:
			aptitud += 1
		
	return aptitud

def seleccion(poblacion):
	'''Elige un elemento de la poblacion por 'ruleta'.

	Recibe:		una lista de listas (poblacion)
	Devuelve:	una lista (individuo)

	Se hace una 'rifa' donde los participantes de la
	'poblacion' obtienen boletos dependiendo de su
	'aptitud', a todos los participantes de les da un
	boleto adicional, esto para garantizar que individuos
	con una aptitud de cero tambien puedan participar.
	'''

	ruleta = []
	boleto = 0

	for individuo in poblacion:
		boleto = func_aptitud(individuo)
		for x in range(0,boleto + 1):
			ruleta.append(individuo)

	return choice(ruleta)

def cruce(ind1, ind2):
	'''Genera nuevo individuo a partir de otros dos.

	Recibe:		Dos listas
	Devuelve:	Una lista

	Si se cumple la condición, se hace el cruce de
	la 'madre' y el 'padre' en el punto de cruce y
	se retorna el 'hijo', de lo contrario se retorna
	la madre.

	Hay condiciones adicionales para evitar que los
	'cromosomas' iniciales sean siempre los de el
	mismo padre.
	'''

	madre = []
	padre = []
	hijo = []

	proba = random()
	punto = randint(0,len(ind1))
	
	if proba > 0.65 :
		madre = ind1
		padre = ind2
	else:
		madre = ind2
		padre = ind1

	if punto == 0:	#Si el punto de cruce esta en los
		punto += 1	#extremos, lo mueve una casilla.
	elif punto == len(ind1):
		punto -= 1

	if proba > 0.3 :
		for x in range(0,punto):
			hijo.append(madre[x])
		for y in range(punto,len(ind2)):
			hijo.append(padre[y])

		hijo = mutacion(hijo)
		return hijo

	else:
		madre = mutacion(madre)
		return madre

def vaciar_lista(lista):
	'''Saca todos los elementos de una lista.

	Rececibe:	Lista con elementos
	Devuelve:	Lista vacia
	'''
	if len(lista) > 0:
		for elemento in range(0,len(lista)):
			lista.pop()

	return lista


def mutacion(individuo):
	
	proba = random()
	mutar1 = randint(0,len(individuo)-1)
	mutar2 = randint(0,len(individuo)-1)
	aux = 0

	'''Esta parte intercambia 2 valores
	if proba < 0.2 and mutar1 != mutar2:
		print("Hubo mutacion en: " + str(individuo))
		aux = individuo[mutar1]
		individuo[mutar1] = individuo[mutar2]
		individuo[mutar2] = aux
	'''

	if proba < 0.05 :
		print("Hubo mutacion en: " + str(individuo))
		individuo[mutar1] = randint(0,len(individuo)-1)

	return(individuo)

main()
