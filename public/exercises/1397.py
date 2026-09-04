# === METADATA ===
# title: Analizador de Calificaciones Escolares
# description: Escribe una función que procese una lista de calificaciones numéricas. Debe iterar sobre la lista y retornar un diccionario que cuente cuántos estudiantes aprobaron (nota >= 60) y cuántos reprobaron (nota < 60), ignorando cualquier valor inválido menor a 0 o mayor a 100.
# difficulty: Intermedio
# expected_output: {'aprobados': 3, 'reprobados': 1}
# hint: Usa un bucle 'for' para recorrer la lista, condicionales 'if-elif' para validar el rango y contar, y un diccionario para almacenar los resultados.

# === SOLUTION ===
def analizar_calificaciones(calificaciones):
    resultado = {"aprobados": 0, "reprobados": 0}
    for nota in calificaciones:
        if 0 <= nota <= 100:
            if nota >= 60:
                resultado["aprobados"] += 1
            else:
                resultado["reprobados"] += 1
    return resultado

# === TESTS ===
try:
    assert analizar_calificaciones([85, 42, 90, 33, 105, -5]) == {'aprobados': 2, 'reprobados': 2}, "Error: el test 1 ha fallado."
    assert analizar_calificaciones([59, 60, 61]) == {'aprobados': 2, 'reprobados': 1}, "Error: considera casos límites en tu lógica."
    assert analizar_calificaciones([10, 20, 30]) == {'aprobados': 0, 'reprobados': 3}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")