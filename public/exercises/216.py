# === METADATA ===
# title: El Analizador de Números Primos y Pares
# description: Escribe una función que tome una lista de números enteros y devuelva una lista nueva con aquellos números que cumplan una condición específica: deben ser números pares y, además, no ser números primos.
# difficulty: Intermedio
# expected_output: [4, 6, 8, 10] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# hint: Recuerda que un número es primo si solo es divisible por 1 y por sí mismo. Puedes crear una lógica auxiliar para verificar si es primo o usar una iteración para contar divisores.

# === SOLUTION ===
def filtrar_pares_no_primos(numeros):
    resultado = []
    for n in numeros:
        if n > 1 and n % 2 == 0:
            es_primo = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    es_primo = False
                    break
            if not es_primo:
                resultado.append(n)
    return resultado

# === TESTS ===
try:
    assert filtrar_pares_no_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 6, 8, 10], "Error: el test 1 ha fallado."
    assert filtrar_pares_no_primos([2, 3, 5, 7, 11]) == [], "Error: no debería incluir números primos."
    assert filtrar_pares_no_primos([0, 1, 12, 14, 15]) == [12, 14], "Error: considera casos límites como el 0 o números compuestos."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")