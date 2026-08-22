# === METADATA ===
# title: Analizador de Calificaciones
# description: Escribe una función que reciba una lista de calificaciones (números enteros del 0 al 100) y devuelva un diccionario con la cantidad de alumnos aprobados (nota >= 60) y reprobados (nota < 60). Si la lista está vacía, debe retornar un mensaje indicando que no hay datos.
# difficulty: Intermedio
# expected_output: {'aprobados': 3, 'reprobados': 2}
# hint: Utiliza un ciclo for para recorrer la lista y condicionales if-else para evaluar cada calificación. No olvides verificar si la lista está vacía al inicio.

# === SOLUTION ===
def analizar_calificaciones(calificaciones):
    if not calificaciones:
        return "No hay datos"
    
    resultados = {"aprobados": 0, "reprobados": 0}
    for nota in calificaciones:
        if nota >= 60:
            resultados["aprobados"] += 1
        else:
            resultados["reprobados"] += 1
            
    return resultados

# === TESTS ===
try:
    assert analizar_calificaciones([85, 42, 90, 55, 70]) == {'aprobados': 3, 'reprobados': 2}, "Error: el test 1 ha fallado."
    assert analizar_calificaciones([59, 30, 45]) == {'aprobados': 0, 'reprobados': 3}, "Error: considera casos límites en tu lógica."
    assert analizar_calificaciones([]) == "No hay datos", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")