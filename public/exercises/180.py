# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero excluyendo aquellos que sean mayores a 20.
# difficulty: Básico
# expected_output: Para la lista [3, 9, 21, 6, 30], el resultado debería ser 18.
# hint: Utiliza un bucle 'for' para recorrer la lista, una estructura 'if' para verificar la divisibilidad (operador módulo %) y el límite superior.

# === SOLUTION ===
def filtrar_y_sumar(lista):
    suma = 0
    for numero in lista:
        if numero % 3 == 0 and numero <= 20:
            suma += numero
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar([3, 9, 21, 6, 30]) == 18, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar([1, 2, 4, 5]) == 0, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar([3, 6, 9, 12, 15, 18]) == 63, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")