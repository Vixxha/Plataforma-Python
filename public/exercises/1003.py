# === METADATA ===
# title: Validador y Sumador de Números Pares
# description: Escribe una función que reciba una lista de números enteros. Debe iterar sobre la lista, utilizar lógica condicional para sumar únicamente los números que sean pares y positivos, y devolver el resultado total de dicha suma. Si la lista no contiene números que cumplan con la condición, debe retornar 0.
# difficulty: Básico
# expected_output: 12
# hint: Utiliza un bucle for para recorrer la lista y una estructura condicional (if) con operadores aritméticos y lógicos (número > 0 y número % 2 == 0) para filtrar los valores antes de sumarlos.

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
    assert sumar_pares_positivos([-2, -4, 0, 3, 7]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_pares_positivos([10, -5, 2, 8, 0]) == 20, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")