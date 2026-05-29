# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe retornar la suma de todos los números en la lista que sean divisibles por el divisor, pero ignorando cualquier número mayor a 100.
# difficulty: Básico
# expected_output: Para ([10, 20, 30, 150], 10) el resultado sería 60.
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' combinando operadores lógicos para filtrar tanto la divisibilidad como el valor máximo permitido.

# === SOLUTION ===
def sumar_filtrados(lista, divisor):
    suma = 0
    for numero in lista:
        if numero % divisor == 0 and numero <= 100:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([10, 20, 30, 150], 10) == 60, "Error: el test 1 ha fallado."
    assert sumar_filtrados([5, 7, 9, 12], 3) == 21, "Error: considera casos límites en tu lógica."
    assert sumar_filtrados([101, 200, 300], 5) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")