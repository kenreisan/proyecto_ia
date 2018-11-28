from random import randint

def main():
	# Aun estoy construllendo las funciones
	print("Y así iniciamos")
	crear_poblacion(16,10)


def crear_poblacion(medida, elementos):
	
	poblacion = []
	pool = []
	inicio = 0
	primer = 1

	for x in range(inicio,medida):
		pool = llenar_pool(elementos)
		poblacion.append([])
		for y in range(inicio,elementos):
			poblacion[x].append(pool.pop(randint(inicio,len(pool)-1)))

	for pob in range(inicio,10):
		print(poblacion[pob])

def llenar_pool(magnitud):

	pool = []
	for x in range(0,magnitud):
		pool.append(x)

	return pool



main()
