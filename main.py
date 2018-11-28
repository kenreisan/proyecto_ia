from random import random, randrange, randint, choice

def main():
	# Aun estoy construllendo las funciones
	poblacion = []
	nueva_gen = []

	print("Y así iniciamos")
	poblacion = crear_poblacion(5,10)

	for x in poblacion:
		#print("\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
		print(x)
		print(str("Aptitud: ") + str(func_aptitud(x)))

	print("\nSeleccion")
	seleccion(poblacion)


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

	ruleta = []
	boleto = 0

	for individuo in poblacion:
		boleto = func_aptitud(individuo)
		for x in range(0,boleto + 1):
			ruleta.append(individuo)

	for objeto in ruleta:
		print(objeto)
	
	print("\n")
	print(choice(ruleta))

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

		return hijo

	else:

		return madre

#print(cruce([1,2,4,6],[3,5,7,8]))
main()
