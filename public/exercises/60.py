# === METADATA ===
# title: Filtrado de Números Primos y Pares
# description: Escribe una función que reciba una lista de números enteros y devuelva una nueva lista que contenga únicamente los números que sean primos y, además, pares. Ten en cuenta las propiedades matemáticas de los números.
# difficulty: Intermedio
# expected_output: [2]
# hint: Recuerda que el único número que es a la vez par y primo es el 2. El resto de números pares son divisibles por 2 y, por tanto, no son primos.

# === SOLUTION ===
def filtrar_primos_pares(lista):
    resultado = []
    for num in lista:
        if num == 2:
            resultado.append(num)
    return resultado

# === TESTS ===
try:
    assert filtrar_primos_pares([1, 2, 3, 4, 5, 6]) == [2], "Error: el test 1 ha fallado."
    assert filtrar_primos_pares([10, 12, 14, 2]) == [2], "Error: considera casos límites en tu lógica."
    assert filtrar_primos_pares([7, 9, 11, 13]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")