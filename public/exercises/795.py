# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y devuelva la suma de aquellos elementos que sean múltiplos de 3, pero excluyendo los múltiplos de 5. Si el número es mayor a 50, se debe sumar solo la mitad de su valor (entero).
# difficulty: Intermedio
# expected_output: 18 (para la lista [3, 5, 9, 15, 60])
# hint: Utiliza un bucle for para recorrer la lista, el operador módulo (%) para verificar múltiplos y recuerda usar la división entera (//) para los números mayores a 50.

# === SOLUTION ===
def procesar_numeros(lista):
    suma = 0
    for num in lista:
        if num % 3 == 0 and num % 5 != 0:
            if num > 50:
                suma += num // 2
            else:
                suma += num
    return suma

# === TESTS ===
try:
    assert procesar_numeros([3, 5, 9, 15, 60]) == 42, "Error: el test 1 ha fallado."
    assert procesar_numeros([10, 20, 25]) == 0, "Error: considera casos límites en tu lógica."
    assert procesar_numeros([3, 6, 60]) == 39, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")