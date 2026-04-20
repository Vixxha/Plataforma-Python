# === METADATA ===
# title: Filtro de Palabras Palíndromas
# description: Crea una función que reciba una lista de cadenas de texto y devuelva una nueva lista que contenga únicamente las palabras que son palíndromas (que se leen igual al derecho y al revés). La comparación debe ignorar mayúsculas y espacios.
# difficulty: Intermedio
# expected_output: ['Radar', 'Anilina']
# hint: Recuerda que puedes invertir un string en Python usando el slicing [::-1] y normalizar el texto con .lower().

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
    assert filtrar_palindromos(["Radar", "Hola", "Anilina", "Python"]) == ["Radar", "Anilina"], "Error: el test 1 ha fallado."
    assert filtrar_palindromos(["oso", "casa", "reconocer"]) == ["oso", "reconocer"], "Error: considera casos límites en tu lógica."
    assert filtrar_palindromos(["mundo", "luna"]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")