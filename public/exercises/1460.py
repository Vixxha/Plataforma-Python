# === METADATA ===
# title: Filtrar y Multiplicar Secuencias
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, aplicar una lógica condicional (si el número es par, multiplicarlo por 2; si es impar, sumarle 3) y retornar una nueva lista con los resultados transformados, pero excluyendo aquellos números originales que sean múltiplos de 5.
# difficulty: Intermedio
# expected_output: [6, 8, 4]
# hint: Usa un bucle `for` para recorrer la lista, una estructura `if-elif-else` para evaluar las condiciones, y un método para agregar elementos a una nueva lista.

# === SOLUTION ===
def transformar_lista(numeros):
    resultado = []
    for num in numeros:
        if num % 5 == 0:
            continue
        elif num % 2 == 0:
            resultado.append(num * 2)
        else:
            resultado.append(num + 3)
    return resultado

# === TESTS ===
try:
    assert transformar_lista([1, 2, 3, 4, 5]) == [4, 4, 6, 8], "Error: el test 1 ha fallado."
    assert transformar_lista([10, 15, 20]) == [], "Error: considera casos límites en tu lógica."
    assert transformar_lista([2, 4, 6]) == [4, 8, 12], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")