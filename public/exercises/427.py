# === METADATA ===
# title: Filtrado y Suma de Múltiplos
# description: Crea una función que reciba una lista de números enteros y un divisor. La función debe sumar únicamente los números de la lista que sean múltiplos del divisor, pero deteniendo el proceso de suma si encuentra un número negativo.
# difficulty: Intermedio
# expected_output: 15 (si la lista es [3, 6, 9, -1, 12] y el divisor es 3)
# hint: Utiliza un bucle for para recorrer la lista, una estructura if para comprobar el múltiplo y la palabra clave break para terminar la iteración ante un número negativo.

# === SOLUTION ===
def sumar_multiplos_hasta_negativo(lista, divisor):
    suma = 0
    for numero in lista:
        if numero < 0:
            break
        if numero % divisor == 0:
            suma += numero
    return suma

# === TESTS ===
try:
    assert sumar_multiplos_hasta_negativo([3, 6, 9, -1, 12], 3) == 18, "Error: el test 1 ha fallado."
    assert sumar_multiplos_hasta_negativo([10, 20, 30], 5) == 60, "Error: considera casos sin números negativos."
    assert sumar_multiplos_hasta_negativo([-5, 10, 15], 5) == 0, "Error: el caso base falló (debe parar al inicio)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")