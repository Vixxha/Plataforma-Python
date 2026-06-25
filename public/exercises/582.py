# === METADATA ===
# title: El Analizador de Números Primos
# description: Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números que sean primos. Un número es primo si es mayor que 1 y solo es divisible por 1 y por sí mismo.
# difficulty: Intermedio
# expected_output: [2, 3, 5, 7]
# hint: Para verificar si un número 'n' es primo, itera desde 2 hasta la raíz cuadrada de 'n' y comprueba si el resto de la división es cero.

# === SOLUTION ===
def filtrar_primos(lista_numeros):
    primos = []
    for n in lista_numeros:
        if n > 1:
            es_primo = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(n)
    return primos

# === TESTS ===
try:
    assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7], "Error: el test 1 ha fallado."
    assert filtrar_primos([11, 13, 17, 19, 20]) == [11, 13, 17, 19], "Error: considera casos límites en tu lógica."
    assert filtrar_primos([0, 1, 4, 6, 8]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")