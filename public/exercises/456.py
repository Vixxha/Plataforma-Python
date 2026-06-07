# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3 o de 5, pero ignorando cualquier número mayor a 100.
# difficulty: Intermedio
# expected_output: 23 (Para la lista [3, 5, 10, 105])
# hint: Utiliza un bucle for para recorrer la lista, un condicional if para verificar la divisibilidad con el operador módulo (%) y otro para restringir el rango del valor.

# === SOLUTION ===
def sumar_multiplos_filtrados(lista):
    suma = 0
    for numero in lista:
        if numero <= 100:
            if numero % 3 == 0 or numero % 5 == 0:
                suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_filtrados([3, 5, 10, 105]) == 18, "Error: el test 1 ha fallado."
    assert sumar_multiplos_filtrados([1, 2, 4, 7]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_filtrados([3, 5, 15, 100]) == 123, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")