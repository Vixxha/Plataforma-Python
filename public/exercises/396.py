# === METADATA ===
# title: Filtrado y Clasificación de Números
# description: Implementa una función que reciba una lista de números enteros. La función debe retornar una nueva lista que contenga solo los números mayores a 10. Si el número es mayor a 10 pero menor o igual a 50, multiplícalo por 2; si es mayor a 50, déjalo tal cual. Los números menores o iguales a 10 deben ser ignorados.
# difficulty: Intermedio
# expected_output: Para la lista [5, 12, 60, 8], el resultado debería ser [24, 60]
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una sentencia 'if' para aplicar la lógica condicional de filtrado y transformación.

# === SOLUTION ===
def procesar_numeros(lista):
    resultado = []
    for num in lista:
        if num > 10:
            if num <= 50:
                resultado.append(num * 2)
            else:
                resultado.append(num)
    return resultado

# === TESTS ===
try:
    assert procesar_numeros([5, 12, 60, 8]) == [24, 60], "Error: el test 1 ha fallado."
    assert procesar_numeros([10, 11, 50, 51]) == [22, 100, 51], "Error: considera casos límites en tu lógica."
    assert procesar_numeros([1, 2, 3]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")