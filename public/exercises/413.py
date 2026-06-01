# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe sumar únicamente los números de la lista que sean múltiplos del divisor dado. Si el divisor es 0, la función debe retornar 0.
# difficulty: Básico
# expected_output: Para ([1, 2, 3, 4, 5, 6], 2) el resultado debería ser 12 (2 + 4 + 6).
# hint: Utiliza un bucle 'for' para recorrer la lista y el operador módulo '%' para verificar la divisibilidad.

# === SOLUTION ===
def sumar_multiplos(lista_numeros, divisor):
    if divisor == 0:
        return 0
    suma = 0
    for numero in lista_numeros:
        if numero % divisor == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos([1, 2, 3, 4, 5, 6], 2) == 12, "Error: el test 1 ha fallado."
    assert sumar_multiplos([10, 15, 20, 25], 5) == 70, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos([1, 3, 7], 2) == 0, "Error: el caso base falló."
    assert sumar_multiplos([1, 2, 3], 0) == 0, "Error: la división por cero no fue manejada."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")