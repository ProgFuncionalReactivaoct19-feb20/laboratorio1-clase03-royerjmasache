"""
	Ejercicio con lista de edades
	@royerjmasache
"""
# Creación de función para evaluar la condición
def function (a):
	# Lista generada con los valores previos
	blackAges = [10, 14, 30, 32, 40, 16]
	# Estructura condicional para evaluar la condiciób
	if a in blackAges:
		# Retorno False para filtrar los elementos que no se encuentran en la lista que se enviará
		return False
	else:
		return True
# Lista con todos los elementos requeridos para la condición
ages = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
# Uso del filter para filtrar los elementos que no cumplen con la condición de la función
whiteAges = filter(function, ages)
# Presentación de resultados en forma de lista
print(list(whiteAges))
