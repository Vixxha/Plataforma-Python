# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que a su vez no sean múltiplos de 5.
# difficulty: Intermedio
# expected_output: 18 (para la lista [3, 6, 9, 15, 20])
# hint: Utiliza un bucle for para recorrer la lista, un operador condicional if con operadores lógicos (and, not) y el operador módulo (%).

# === SOLUTION ===
def sumar_filtrados(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 3 == 0 and numero % 5 != 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_filtrados([3, 6, 9, 15, 20]) == 18, "Error: el test 1 ha fallado."
    assert sumar_filtrados([10, 20, 25]) == 0, "Error: considera casos donde no hay múltiplos válidos."
    assert sumar_filtrados([3, 5, 30, 33]) == 36, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")