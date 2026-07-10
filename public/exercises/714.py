# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe retornar la suma de todos los números en la lista que sean divisibles por el divisor proporcionado, pero ignorando cualquier número que sea mayor a 100.
# difficulty: Intermedio
# expected_output: 30 (para la lista [5, 10, 15, 120] y divisor 5)
# hint: Utiliza un bucle 'for' para recorrer la lista, una estructura 'if' para verificar la divisibilidad (operador módulo %) y otra condición para filtrar valores mayores a 100.

# === SOLUTION ===
def sumar_multiplos_filtrados(lista, divisor):
    suma = 0
    for numero in lista:
        if numero <= 100 and numero % divisor == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_filtrados([5, 10, 15, 120], 5) == 30, "Error: el test 1 ha fallado."
    assert sumar_multiplos_filtrados([10, 20, 101, 200], 10) == 30, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_filtrados([7, 14, 21], 3) == 21, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")