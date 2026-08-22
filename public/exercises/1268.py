# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista y sumar únicamente aquellos números que sean pares y además sean mayores que cero. Si encuentra el número 999, debe detener la iteración inmediatamente (romper el ciclo). La función debe retornar la suma total acumulada.
# difficulty: Intermedio
# expected_output: 12
# hint: Usa un bucle 'for' o 'while', una estructura condicional 'if' para verificar las condiciones, y la instrucción 'break' para detener la ejecución al encontrar el 999.

# === SOLUTION ===
def procesar_numeros_pares(numeros):
    suma = 0
    for num in numeros:
        if num == 999:
            break
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert procesar_numeros_pares([2, 4, -2, 6, 999, 8]) == 12, "Error: el test 1 ha fallado."
    assert procesar_numeros_pares([1, 3, 5, 7, 999, 2, 4]) == 0, "Error: considera casos límites en tu lógica."
    assert procesar_numeros_pares([10, -4, 2, 8]) == 20, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")