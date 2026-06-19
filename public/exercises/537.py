# === METADATA ===
# title: Filtrado de Números Primos y Suma
# description: Escribe una función que reciba una lista de números enteros y devuelva la suma exclusiva de aquellos elementos que sean números primos.
# difficulty: Intermedio
# expected_output: 17 (para la lista [1, 2, 3, 4, 5, 7])
# hint: Un número primo es mayor a 1 y solo es divisible por 1 y por sí mismo. Puedes usar un bucle anidado o una estructura de control para verificar la divisibilidad.

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
    assert sumar_primos([10, 15, 20]) == 0, "Error: considera casos límites en tu lógica."
    assert sumar_primos([2, 3, 11]) == 16, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")