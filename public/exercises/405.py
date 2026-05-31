# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que a su vez no sean múltiplos de 5.
# difficulty: Básico
# expected_output: Para la lista [3, 5, 9, 15, 18], el resultado debería ser 30 (3 + 9 + 18).
# hint: Utiliza un bucle for para recorrer la lista, un operador condicional if con el operador módulo (%) y un acumulador.

# === SOLUTION ===
def filtrar_y_sumar(numeros):
    suma = 0
    for n in numeros:
        if n % 3 == 0 and n % 5 != 0:
            suma += n
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar([3, 5, 9, 15, 18]) == 30, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar([1, 2, 4, 7]) == 0, "Error: considera casos donde no hay múltiplos válidos."
    assert filtrar_y_sumar([3, 6, 9, 12, 15, 30]) == 30, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")