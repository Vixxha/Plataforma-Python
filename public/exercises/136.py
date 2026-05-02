# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero descartando cualquier número que sea negativo.
# difficulty: Intermedio
# expected_output: 23 (Para la lista [3, 5, -9, 10, 2, 7])
# hint: Utiliza un bucle 'for' para recorrer la lista, una estructura 'if' con operadores lógicos ('or') para verificar las condiciones y una variable acumuladora.

# === SOLUTION ===
def sumar_multiplos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and (num % 3 == 0 or num % 5 == 0):
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_multiplos([3, 5, -9, 10, 2, 7]) == 18, "Error: el test 1 ha fallado."
    assert sumar_multiplos([15, 30, -5, 0]) == 45, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos([1, 2, 4, 7]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")