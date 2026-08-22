# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, verificar mediante lógica condicional si cada número es par y positivo, y retornar la suma acumulada de dichos números. Si la lista está vacía o no hay números que cumplan la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 30
# hint: Utiliza un bucle for para recorrer la lista, y una estructura condicional (if) combinando operadores de comparación y módulo (%) para filtrar los números pares y positivos.

# === SOLUTION ===
def suma_pares_positivos(numeros):
    suma = 0
    for num in numeros:
        if num > 0 and num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert suma_pares_positivos([1, 2, 3, 4, 5, 6]) == 12, "Error: el test 1 ha fallado."
    assert suma_pares_positivos([-2, -4, 0, 5, 10, 15]) == 10, "Error: considera casos límites en tu lógica."
    assert suma_pares_positivos([]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")