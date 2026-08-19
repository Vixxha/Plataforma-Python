# === METADATA ===
# title: Analizador de Calificaciones
# description: Escribe una función que reciba una lista de calificaciones numéricas (enteros o flotantes entre 0 y 100). Utilizando bucles y lógica condicional, la función debe procesar la lista y retornar una cadena con la categoría general del grupo según las siguientes reglas: si el promedio es mayor o igual a 90, retorna 'Excelente'; si es mayor o igual a 75 y menor a 90, retorna 'Bueno'; si es mayor o igual a 60 y menor a 75, retorna 'Aprobado'; y si es menor a 60, retorna 'Reprobado'. Si la lista está vacía, debe retornar 'Sin datos'.
# difficulty: Intermedio
# expected_output: 'Bueno'
# hint: Recuerda validar primero si la lista está vacía para evitar errores al calcular el promedio. Usa un bucle para sumar los elementos y luego divide entre la cantidad total.

# === SOLUTION ===
def analizar_calificaciones(calificaciones):
    if not calificaciones:
        return "Sin datos"
    
    suma = 0
    for nota in calificaciones:
        suma += nota
        
    promedio = suma / len(calificaciones)
    
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 75:
        return "Bueno"
    elif promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

# === TESTS ===
try:
    assert analizar_calificaciones([95, 85, 90, 100]) == "Excelente", "Error: el test 1 ha fallado."
    assert analizar_calificaciones([70, 65, 80]) == "Bueno", "Error: considera casos límites en tu lógica."
    assert analizar_calificaciones([]) == "Sin datos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")