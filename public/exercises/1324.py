# === METADATA ===
# title: Filtrar y Contar Números Válidos
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, filtrar los números que sean pares y mayores que 10, y retornar una lista con los cuadrados de dichos números.
# difficulty: Intermedio
# expected_output: [144, 196]
# hint: Utiliza un bucle for o comprensión de listas combinando condiciones con el operador módulo (%).

# === SOLUTION ===
def procesar_numeros(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0 and num > 10:
            resultado.append(num ** 2)
    return resultado

# === TESTS ===
try:
    assert procesar_numeros([4, 12, 5, 14, 8]) == [144, 196], "Error: el test 1 ha fallado."
    assert procesar_numeros([2, 6, 9]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_numeros([10, 16, 20]) == [256, 400], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")