# === METADATA ===
# title: Filtrar y Sumar Números Pares
# description: Escribe una función que reciba una lista de números enteros, filtre únicamente aquellos que sean pares y devuelva la suma total de dichos números. Si no hay números pares, debe devolver 0.
# difficulty: Básico
# expected_output: 12
# hint: Puedes usar un bucle `for` o una comprensión de lista combinada con el operador módulo `%` para verificar si un número es par.

# === SOLUTION ===
def sumar_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares([1, 2, 3, 4, 5, 6]) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares([1, 3, 5, 7]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares([-2, -4, 5, 8]) == 2, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")