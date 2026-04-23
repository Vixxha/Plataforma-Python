# === METADATA ===
# title: Filtro de Palabras Palíndromas
# description: Crea una función que reciba una lista de palabras y retorne una nueva lista que contenga solo aquellas palabras que son palíndromas (se leen igual al derecho que al revés), ignorando mayúsculas y espacios.
# difficulty: Intermedio
# expected_output: ['Radar', 'Ana', 'Ojo']
# hint: Recuerda que puedes invertir un string usando el slicing [::-1] y normalizar el texto con .lower().

# === SOLUTION ===
def filtrar_palindromos(lista_palabras):
    resultado = []
    for palabra in lista_palabras:
        limpia = palabra.replace(" ", "").lower()
        if limpia == limpia[::-1]:
            resultado.append(palabra)
    return resultado

# === TESTS ===
try:
    assert filtrar_palindromos(["Radar", "Hola", "Ana", "Python", "Ojo"]) == ["Radar", "Ana", "Ojo"], "Error: el test 1 ha fallado."
    assert filtrar_palindromos(["oso", "casa", "reconocer"]) == ["oso", "reconocer"], "Error: considera casos límites en tu lógica."
    assert filtrar_palindromos(["mundo", "test"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")