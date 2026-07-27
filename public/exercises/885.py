# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista, identificar los números pares, multiplicarlos por 3 y retornar una nueva lista con estos resultados transformados.
# difficulty: Básico
# expected_output: [6, 12, 18]
# hint: Utiliza un bucle for para recorrer la lista y una condición if con el operador módulo (%) para verificar si un número es par.

# === SOLUTION ===
def procesar_pares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num * 3)
    return resultado

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4, 5, 6]) == [6, 12, 18], "Error: el test 1 ha fallado."
    assert procesar_pares([1, 3, 5]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_pares([2, 4]) == [6, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")