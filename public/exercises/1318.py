# === METADATA ===
# title: Analizador de Calificaciones
# description: Escribe una función que reciba una lista de calificaciones numéricas (entre 0 y 100). La función debe iterar sobre la lista, ignorar cualquier valor inválido (menor que 0 o mayor que 100), y retornar el promedio de las calificaciones válidas redondeado a 2 decimales. Si no hay calificaciones válidas, debe retornar 0.0.
# difficulty: Intermedio
# expected_output: 85.5
# hint: Usa un bucle 'for' para recorrer la lista, condicionales 'if' para filtrar los valores válidos, y acumula la suma y el conteo para calcular el promedio.

# === SOLUTION ===
def calcular_promedio_valido(calificaciones):
    suma = 0
    contador = 0
    for nota in calificaciones:
        if 0 <= nota <= 100:
            suma += nota
            contador += 1
    if contador == 0:
        return 0.0
    return round(suma / contador, 2)

# === TESTS ===
try:
    assert calcular_promedio_valido([80, 90, 105, -5, 100]) == 90.0, "Error: el test 1 ha fallado."
    assert calcular_promedio_valido([-10, 150, 200]) == 0.0, "Error: considera casos límites en tu lógica."
    assert calcular_promedio_valido([70, 80, 90]) == 80.0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")