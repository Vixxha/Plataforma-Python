# === METADATA ===
# title: Filtrado de números primos
# description: Crea una función que reciba una lista de números enteros y retorne una nueva lista que contenga solo los números primos presentes en la lista original. Un número primo es aquel mayor a 1 que solo es divisible por sí mismo y por 1.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# hint: Recuerda usar un bucle anidado o una estructura iterativa para verificar los divisores de cada número desde 2 hasta la raíz cuadrada del mismo.

# === SOLUTION ===
def filtrar_primos(lista):
    resultado = []
    for numero in lista:
        if numero > 1:
            es_primo = True
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                resultado.append(numero)
    return resultado

# === TESTS ===
try:
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19, 20]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([0, 1, 4, 6, 8]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")