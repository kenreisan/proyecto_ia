from random import randint

def main():
	# Aun estoy construllendo las funciones
	print("Y así iniciamos")
	crear_poblacion(16,10)


def crear_poblacion(medida, elementos):
	
	poblacion = []
	inicio = 0

	for x in range(inicio,medida):
		poblacion.append([])
		for y in range(inicio,elementos):
			poblacion[x].append(randint(inicio,elementos))

	for pob in range(inicio,10):
		print(poblacion[pob])





main()
