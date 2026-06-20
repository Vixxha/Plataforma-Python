# === METADATA ===
# title: Filtrado y Suma Condicional de Números
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números positivos que sean múltiplos de 3, ignorando cualquier número negativo o impar.
# difficulty: Intermedio
# expected_output: 18 (para la lista [1, 3, 6, -9, 9, 10])
# hint: Utiliza un bucle for para iterar sobre la lista y un condicional if con el operador módulo (%) para verificar las condiciones.

# === SOLUTION ===
def sumar_multiplos_tres(lista):
    suma = 0
    for numero in lista:
        if numero > 0 and numero % 3 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_tres([1, 3, 6, -9, 9, 10]) == 18, "Error: el test 1 ha fallado."
    assert sumar_multiplos_tres([-3, -6, -9]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_tres([0, 12, 15, 2]) == 27, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")