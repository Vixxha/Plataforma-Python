# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, identificar los números pares, multiplicarlos por 3, y retornar una nueva lista con estos resultados transformados. Si la lista está vacía o no hay números pares, debe retornar una lista vacía.
# difficulty: Básico
# expected_output: [6, 12]
# hint: Utiliza un bucle 'for' para recorrer los elementos y una estructura condicional 'if' con el operador módulo (%) para verificar si un número es par.

# === SOLUTION ===
def procesar_pares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num * 3)
    return resultado

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4]) == [6, 12], "Error: el test 1 ha fallado."
    assert procesar_pares([5, 7, 9]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_pares([2, 4, 6]) == [6, 12, 18], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")