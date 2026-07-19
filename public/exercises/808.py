# === METADATA ===
# title: Filtrado de números y cálculo de promedio
# description: Crea una función que reciba una lista de números enteros. La función debe sumar únicamente los números que sean pares y mayores a 10, y devolver el promedio de esos números específicos. Si no hay números que cumplan la condición, debe retornar 0.
# difficulty: Intermedio
# expected_output: 15.0
# hint: Utiliza un bucle for para iterar y contadores separados para la suma acumulada y la cantidad de elementos que cumplen la condición.

# === SOLUTION ===
def procesar_numeros(lista):
    suma = 0
    contador = 0
    for num in lista:
        if num > 10 and num % 2 == 0:
            suma += num
            contador += 1
    
    if contador == 0:
        return 0
    return suma / contador

# === TESTS ===
try:
    assert procesar_numeros([4, 12, 18, 5, 20]) == 16.666666666666668, "Error: el promedio calculado no es correcto."
    assert procesar_numeros([1, 3, 5, 7]) == 0, "Error: debería retornar 0 si no hay números que cumplan la condición."
    assert procesar_numeros([10, 20, 30]) == 25.0, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")