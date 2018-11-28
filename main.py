from random import randint

def main():
	# Aun estoy construllendo las funciones
	poblacion = []

	print("Y así iniciamos")
	poblacion = crear_poblacion(16,10)

	
	for x in poblacion[0]:
		print("\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
		print(poblacion[x])
		print(str("Aptitud: ") + func_aptitud(poblacion[x]))


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

main()
