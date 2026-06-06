# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5. Si el número es múltiplo de ambos, solo debe contarse una vez.
# difficulty: Intermedio
# expected_output: 33 (para la entrada [1, 3, 5, 10, 15, 2])
# hint: Utiliza un bucle for para iterar y el operador módulo (%) para verificar las condiciones dentro de una estructura if-elif.

# === SOLUTION ===
def sumar_multiplos(lista):
    suma_total = 0
    for numero in lista:
        if numero % 3 == 0 or numero % 5 == 0:
            suma_total += numero
    return suma_total

# === TESTS ===
try:
    assert sumar_multiplos([1, 3, 5, 10, 15, 2]) == 33, "Error: el test 1 ha fallado."
    assert sumar_multiplos([3, 6, 9]) == 18, "Error: considera casos donde solo hay múltiplos de 3."
    assert sumar_multiplos([0, 1, 2]) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")