# === METADATA ===
# title: Filtrado y Suma Condicional
# description: Crea una función que reciba una lista de números y devuelva la suma de todos los números que sean mayores a 10 y, al mismo tiempo, sean pares. Si no hay números que cumplan ambas condiciones, la función debe devolver 0.
# difficulty: Básico
# expected_output: 30 (para la lista [5, 12, 8, 18, 20, 7])
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' con operadores lógicos (and) para verificar las dos condiciones simultáneamente.

# === SOLUTION ===
def filtrar_y_sumar(lista):
    suma = 0
    for numero in lista:
        if numero > 10 and numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert filtrar_y_sumar([5, 12, 8, 18, 20, 7]) == 50, "Error: el test 1 ha fallado."
    assert filtrar_y_sumar([1, 3, 5, 7]) == 0, "Error: considera casos límites en tu lógica."
    assert filtrar_y_sumar([10, 11, 22]) == 22, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")