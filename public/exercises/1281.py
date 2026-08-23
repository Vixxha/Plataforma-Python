# === METADATA ===
# title: Filtrar y Sumar Impares con Límite
# description: Escribe una función que reciba una lista de números enteros y un valor límite. La función debe iterar sobre la lista, evaluar condicionalmente si cada número es impar y estrictamente menor que el límite, y retornar la suma de dichos números. Si ningún número cumple la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 16
# hint: Usa un bucle 'for' para recorrer los elementos, una estructura condicional 'if' con el operador módulo (%) para verificar si es impar, y un acumulador.

# === SOLUTION ===
def sumar_impares_con_limite(numeros, limite):
    suma = 0
    for num in numeros:
        if num % 2 != 0 and num < limite:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_impares_con_limite([1, 2, 3, 5, 9, 10], 8) == 9, "Error: el test 1 ha fallado."
    assert sumar_impares_con_limite([2, 4, 6, 8], 10) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_impares_con_limite([5, 5, 5, 12], 10) == 15, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")