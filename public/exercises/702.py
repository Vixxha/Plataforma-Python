# === METADATA ===
# title: Filtrado y Suma Condicional de Números
# description: Crea una función que reciba una lista de números enteros. La función debe devolver la suma de todos los números positivos que sean divisibles por 3, ignorando cualquier número negativo o impar.
# difficulty: Intermedio
# expected_output: 18 (para la lista [1, 3, 6, -9, 9, 4, 12, 0])
# hint: Utiliza un bucle for para iterar sobre la lista y un condicional if para verificar si el número es mayor a cero y si el residuo al dividirlo por 3 es igual a 0.

# === SOLUTION ===
def sumar_multiplos_de_tres(lista):
    suma = 0
    for numero in lista:
        if numero > 0 and numero % 3 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_de_tres([1, 3, 6, -9, 9, 4, 12, 0]) == 30, "Error: el test 1 ha fallado."
    assert sumar_multiplos_de_tres([-3, -6, -9]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_de_tres([3, 3, 3]) == 9, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")