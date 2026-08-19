# === METADATA ===
# title: Filtrar y Multiplicar Secuencia Numérica
# description: Escribe una función que reciba una lista de números enteros. La función debe iterar sobre la lista y aplicar la siguiente lógica condicional a cada número: si el número es par y mayor a cero, multiplícalo por 2; si es impar y mayor a cero, súmale 3; ignora cualquier número menor o igual a cero. La función debe retornar una nueva lista con los resultados obtenidos.
# difficulty: Intermedio
# expected_output: [4, 6, 8] para la entrada [-2, 0, 1, 2, 3]
# hint: Usa un bucle 'for' para recorrer los elementos y una estructura 'if-elif-else' junto con el operador módulo (%) para verificar si un número es par o impar.

# === SOLUTION ===
def procesar_numeros(numeros):
    resultado = []
    for num in numeros:
        if num > 0:
            if num % 2 == 0:
                resultado.append(num * 2)
            else:
                resultado.append(num + 3)
    return resultado

# === TESTS ===
try:
    assert procesar_numeros([-2, 0, 1, 2, 3]) == [4, 4, 6], "Error: el test 1 ha fallado."
    assert procesar_numeros([-5, -1, 4, 6]) == [8, 12], "Error: considera casos límites en tu lógica."
    assert procesar_numeros([5, 7, 9]) == [8, 10, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")