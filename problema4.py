"""
	Ejercicio de calificación cualitativa
	@royerjmasache
"""
# Creación de lista con los valores a evaluar
grades = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
# Uso del filter para filtrar los resultados a obtener y función lambda para recorrer la lista y evaluar  la condición
result = filter(lambda a: a[3] == "Regular" or a[3] == "Bueno", grades)
# Presentación de resultados en forma de lista
print(list(result))

