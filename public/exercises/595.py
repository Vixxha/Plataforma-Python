# === METADATA ===
# title: El Analizador de Números Primos y Pares
# description: Escribe una función que tome una lista de números enteros y devuelva un diccionario con dos claves: 'primos' y 'pares'. La lista 'primos' debe contener todos los números primos de la entrada, y 'pares' todos los números divisibles por 2. Un número puede pertenecer a ambas listas.
# difficulty: Intermedio
# expected_output: {'primos': [2, 3, 5], 'pares': [2, 4, 6]}
# hint: Recuerda que un número primo es aquel mayor a 1 que solo tiene dos divisores: 1 y sí mismo. Puedes iterar por la lista y usar condicionales para clasificar cada elemento.

# === SOLUTION ===
def clasificador_numeros(lista):
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    resultado = {'primos': [], 'pares': []}
    for num in lista:
        if es_primo(num):
            resultado['primos'].append(num)
        if num % 2 == 0:
            resultado['pares'].append(num)
    return resultado

# === TESTS ===
try:
    assert clasificador_numeros([1, 2, 3, 4, 5, 6]) == {'primos': [2, 3, 5], 'pares': [2, 4, 6]}, "Error: el test 1 ha fallado."
    assert clasificador_numeros([10, 11, 13, 14]) == {'primos': [11, 13], 'pares': [10, 14]}, "Error: considera casos límites en tu lógica."
    assert clasificador_numeros([0, 1]) == {'primos': [], 'pares': [0]}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")