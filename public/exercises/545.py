# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que a su vez no sean múltiplos de 5.
# difficulty: Básico
# expected_output: Para la entrada [3, 5, 6, 9, 15, 12], la salida debe ser 30 (3+6+9+12).
# hint: Utiliza un bucle for para recorrer la lista, un operador condicional if con el operador módulo (%) para verificar los múltiplos y una variable acumuladora.

# === SOLUTION ===
def sumar_filtrados(numeros):
    suma = 0
    for num in numeros:
        if num % 3 == 0 and num % 5 != 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([3, 5, 6, 9, 15, 12]) == 30, "Error: el test 1 ha fallado."
    assert sumar_filtrados([1, 2, 4, 7]) == 0, "Error: considera casos donde no hay múltiplos."
    assert sumar_filtrados([3, 6, 15, 30]) == 9, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")