# === METADATA ===
# title: Filtrar y Multiplicar Números Pares
# description: Escribe una función que reciba una lista de enteros. La función debe iterar sobre la lista, identificar los números pares, multiplicarlos por 3 y retornar una nueva lista con estos valores transformados en el mismo orden de aparición.
# difficulty: Básico
# expected_output: [6, 12]
# hint: Usa un bucle 'for' para recorrer los elementos y una condición 'if' con el operador módulo (%) para verificar si un número es par.

# === SOLUTION ===
def procesar_pares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num * 3)
    return resultado

# === TESTS ===
try:
    assert procesar_pares([1, 2, 3, 4, 5]) == [6, 12], "Error: el test 1 ha fallado."
    assert procesar_pares([10, 15, 20]) == [30, 60], "Error: considera casos límites en tu lógica."
    assert procesar_pares([1, 3, 5]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")