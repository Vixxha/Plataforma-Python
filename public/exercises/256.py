# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: 33 (para la lista [3, 5, 10, 15, 120])
# hint: Utiliza un bucle for para recorrer la lista, un condicional if con operadores lógicos (or) y una variable acumuladora.

# === SOLUTION ===
def sumar_multiplos(numeros):
    suma = 0
    for n in numeros:
        if n <= 100 and (n % 3 == 0 or n % 5 == 0):
            suma += n
    return suma

# === TESTS ===
try:
    assert sumar_multiplos([3, 5, 10, 15, 120]) == 33, "Error: el test 1 ha fallado."
    assert sumar_multiplos([1, 2, 4, 7, 8]) == 0, "Error: debería devolver 0 si no hay múltiplos."
    assert sumar_multiplos([30, 105, 9]) == 39, "Error: considera casos límites como números mayores a 100."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")