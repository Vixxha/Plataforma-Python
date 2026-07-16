# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero que no sean múltiplos de 5. Si el número es mayor a 50, se debe ignorar independientemente de su divisibilidad.
# difficulty: Intermedio
# expected_output: 18 (para una entrada como [3, 6, 9, 15, 55])
# hint: Utiliza un bucle 'for' para iterar, el operador módulo '%' para verificar divisibilidad y una estructura 'if' con operadores lógicos 'and'/'not'.

# === SOLUTION ===
def procesar_numeros(lista):
    suma = 0
    for numero in lista:
        if numero <= 50 and numero % 3 == 0 and numero % 5 != 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert procesar_numeros([3, 6, 9, 15, 55]) == 18, "Error: el test 1 ha fallado."
    assert procesar_numeros([10, 20, 30, 40]) == 0, "Error: considera casos límites en tu lógica."
    assert procesar_numeros([3, 5, 51, 12, 18]) == 33, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")