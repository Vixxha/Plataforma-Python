# === METADATA ===
# title: Filtrado y Suma de Números Primos
# description: Escribe una función que reciba una lista de números enteros y devuelva la suma de todos los números dentro de la lista que sean números primos.
# difficulty: Intermedio
# expected_output: 17 (para la lista [1, 2, 3, 4, 5, 7])
# hint: Un número es primo si es mayor a 1 y solo es divisible entre 1 y sí mismo. Puedes usar un bucle for para verificar los divisores.

# === SOLUTION ===
def sumar_primos(lista):
    suma = 0
    for num in lista:
        if num > 1:
            es_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                suma += num
    return suma

# === TESTS ===
try:
    assert sumar_primos([1, 2, 3, 4, 5, 7]) == 17, "Error: el test 1 ha fallado."
    assert sumar_primos([10, 15, 20]) == 0, "Error: considera casos donde no hay primos."
    assert sumar_primos([2, 11, 13]) == 26, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")