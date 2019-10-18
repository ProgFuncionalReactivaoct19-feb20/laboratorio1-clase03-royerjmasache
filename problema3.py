"""
	Ejercicio con frase
	@royerjmasache
"""
# Creación de función para evaluar la condición
def function (a):
	# Lista con los elementos que se desea filtrar
	words = ["No", "hay", "que", "lo", "que", "no", "la"]
	# Estructura condicional para evaluar la condición
	if a in words:
		return True
	else:
		return False
# Variable que almacena el valor de la frase
phrase = "No hay medicina que cure lo que no cura la felicidad"
# Creación de variable almacenadora y uso de .split para separar en elementos el valor de la variable
separator = phrase.split()
# Uso del filter para obtener los resultados
result = filter(function, separator)
# Presentación de resultados en forma de lista
print(list(result))
