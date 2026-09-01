# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, verificar mediante lógica condicional cuáles números son pares y positivos, y devolver la suma total de dichos números. Si la lista está vacía o no hay números que cumplan la condición, debe retornar 0.
# difficulty: Básico
# expected_output: 30
# hint: Usa un bucle 'for' para recorrer la lista, una estructura 'if' para comprobar si el número es mayor que cero y divisible por dos (usando el operador módulo %), y acumula el resultado en una variable.

# === SOLUTION ===
def sumar_pares_positivos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert sumar_pares_positivos([1, 2, 3, 4, 5, 6]) == 12, "Error: el test 1 ha fallado."
    assert sumar_pares_positivos([-2, 4, 6, -8, 10]) == 20, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos([-1, -3, -5, 0]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")