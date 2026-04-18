# === METADATA ===
# title: Suma de Números Pares
# description: Escribe una función llamada 'suma_pares' que reciba una lista de números enteros y retorne la suma de todos los números que sean pares. Ignora los impares.
# expected_output: Para la lista [1, 2, 3, 4, 5, 6], el resultado esperado es 12.
# hint: Usa el operador módulo (%) para verificar si un número es par: num % 2 == 0.

# === SOLUTION ===
def suma_pares(numeros):
    suma = 0
    for num in numeros:
        if num % 2 == 0:
            suma += num
    return suma

# === TESTS ===
try:
    assert suma_pares([1, 2, 3, 4, 5, 6]) == 12, "Error: La suma debe ser 12"
    assert suma_pares([1, 3, 5]) == 0, "Error: Si no hay pares, debe devolver 0"
    assert suma_pares([-2, 4, 3]) == 2, "Error: Debe sumar correctamente números negativos"
    assert suma_pares([]) == 0, "Error: Lista vacía debe devolver 0"
except NameError:
    raise AssertionError("La función 'suma_pares' no está definida.")