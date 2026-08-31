# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que tome una lista de números enteros, filtre únicamente los números pares, y devuelva una nueva lista donde cada uno de estos números pares haya sido multiplicado por 2. Si no hay números pares, debe devolver una lista vacía.
# difficulty: Básico
# expected_output: [4, 8]
# hint: Puedes utilizar un bucle `for` o una lista por comprensión (list comprehension) combinada con el operador módulo `%` para verificar si un número es par.

# === SOLUTION ===
def procesar_pares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num * 2)
    return resultado

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4]) == [4, 8], "Error: el test 1 ha fallado."
    assert procesar_pares([5, 7, 9]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_pares([-2, 0, 3, 6]) == [-4, 0, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")