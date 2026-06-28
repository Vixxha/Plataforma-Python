# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe retornar la suma de todos los números de la lista que sean múltiplos del divisor. Si el número es mayor a 100, debe ignorarse aunque sea múltiplo.
# difficulty: Intermedio
# expected_output: 30 (Para la lista [5, 10, 15, 120] y divisor 5, ya que 5+10+15=30)
# hint: Utiliza un bucle 'for' para recorrer la lista, un operador de módulo (%) para verificar divisibilidad y una estructura condicional 'if' para validar ambas condiciones.

# === SOLUTION ===
def sumar_multiplos_filtrados(lista, divisor):
    suma = 0
    for numero in lista:
        if numero % divisor == 0 and numero <= 100:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_filtrados([5, 10, 15, 120], 5) == 30, "Error: el test 1 ha fallado."
    assert sumar_multiplos_filtrados([2, 4, 6, 8, 10], 2) == 30, "Error: considera casos límites en tu lógica."
    assert sumar_multiplos_filtrados([101, 202, 303], 3) == 0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")