"""
	Ejercicio con uso de lista
	@royerjmasache
"""
# Creación de lista con los datos
grades = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
# Uso de función anónima para evaluar sumar los valores en cada una de las posiciones
result = lambda a: a[0] + a[1] + a[2]
# Uso del map para iterar en los valores de la lista y presentación de resultados
print(list(map(result, grades)))
