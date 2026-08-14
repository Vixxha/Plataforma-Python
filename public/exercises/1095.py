# === METADATA ===
# title: Filtrar y Sumar Números Pares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, verificar mediante lógica condicional si cada número es par y positivo, y retornar la suma total de dichos números. Si la lista está vacía o no hay números que cumplan la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 20
# hint: Usa un bucle 'for' para recorrer la lista y una condición 'if' con los operadores aritméticos y lógicos adecuados (número > 0 y número % 2 == 0).

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
    assert sumar_pares_positivos([-2, 4, 0, 8, -6]) == 12, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos([-1, -3, -5, 0]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")