# === METADATA ===
# title: El Analizador de Números Primos y Pares
# description: Escribe una función que tome una lista de números enteros y devuelva una lista con aquellos que cumplen al menos una de estas dos condiciones: que sean números pares o que sean números primos.
# difficulty: Intermedio
# expected_output: [2, 3, 4, 5, 7, 10] para la entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# hint: Crea una función auxiliar o utiliza lógica booleana para verificar la primalidad antes de iterar sobre la lista. Recuerda que el 1 no es primo.

# === SOLUTION ===
def filtrar_numeros(lista):
    resultado = []
    for n in lista:
        es_par = (n % 2 == 0)
        es_primo = False
        if n > 1:
            es_primo = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    es_primo = False
                    break
        if es_par or es_primo:
            resultado.append(n)
    return resultado

# === TESTS ===
try:
    assert filtrar_numeros([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 10], "Error: el test 1 ha fallado."
    assert filtrar_numeros([1, 9, 15]) == [], "Error: el caso sin primos ni pares falló."
    assert filtrar_numeros([2, 11, 13]) == [2, 11, 13], "Error: el caso solo con números primos falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")