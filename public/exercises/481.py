# === METADATA ===
# title: Filtrado de números y cálculo de suma
# description: Crea una función que reciba una lista de números enteros. La función debe sumar únicamente aquellos números que sean positivos y pares. Si la lista está vacía o no contiene números que cumplan la condición, debe retornar 0.
# difficulty: Básico
# expected_output: 12 (para la entrada [1, 2, 4, 5, 6, -2, -4])
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' con el operador módulo (%) para verificar si el número es par y mayor a cero simultáneamente.

# === SOLUTION ===
def sumar_pares_positivos(lista):
    suma = 0
    for numero in lista:
        if numero > 0 and numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_pares_positivos([1, 2, 4, 5, 6, -2, -4]) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares_positivos([-1, -3, -5]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos([]) == 0, "Error: el caso base falló."
    assert sumar_pares_positivos([10, 3, 8]) == 18, "Error: el test 4 ha fallado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")