# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que no sean múltiplos de 5. Si el número es mayor a 50, se debe ignorar independientemente de si cumple la condición anterior.
# difficulty: Intermedio
# expected_output: 18 (para la lista [3, 5, 6, 9, 15, 51])
# hint: Utiliza un bucle for para iterar y operadores de módulo (%) junto con condicionales if/and/not para filtrar.

# === SOLUTION ===
def filtrar_y_sumar(numeros):
    suma = 0
    for n in numeros:
        if n <= 50 and n % 3 == 0 and n % 5 != 0:
            suma += n
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar([3, 5, 6, 9, 15, 51]) == 18, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar([30, 45, 10, 2]) == 0, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar([3, 6, 12, 18]) == 39, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")