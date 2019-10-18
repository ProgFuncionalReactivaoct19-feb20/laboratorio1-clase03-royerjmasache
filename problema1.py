"""
	Ejercicio del promedio
	@royerjmasache
"""
# Creación de arreglo con los promedios de los estudiantes
averages = [10, 20, 18, 19, 20, 17, 18, 16, 16, 11, 12, 13]
# Uso del filter para filtrar los datos y de función lambda para evaluar la condición
result = filter(lambda a: a >= 16.5, averages)
# Presentación de resultados
print(list(result))
