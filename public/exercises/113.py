# === METADATA ===
# title: Filtrado y Suma Condicional
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números que sean positivos y pares. Si la lista está vacía o no hay números que cumplan la condición, la función debe devolver 0.
# difficulty: Básico
# expected_output: [12] para una entrada de [1, 2, 4, -6, 6, 3, 0]
# hint: Utiliza un bucle 'for' para iterar sobre la lista y una estructura 'if' con operadores lógicos para verificar si el número es mayor a cero y divisible por dos (usando el operador módulo %).

# === SOLUTION ===
def sumar_positivos_pares(lista):
    suma = 0
    for numero in lista:
        if numero > 0 and numero % 2 == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_positivos_pares([1, 2, 4, -6, 6, 3, 0]) == 12, "Error: el test 1 ha fallado."
    assert sumar_positivos_pares([-2, -4, -8]) == 0, "Error: considera casos donde todos son negativos."
    assert sumar_positivos_pares([]) == 0, "Error: el caso base de lista vacía falló."
    assert sumar_positivos_pares([10, 11, 12]) == 22, "Error: suma incorrecta."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")