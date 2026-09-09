# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados en una elección y devuelva un diccionario con el conteo de votos de cada uno. Además, si hay votos, debe identificar y retornar el nombre del candidato ganador. Para este ejercicio intermedio, retorna una tupla con el diccionario de conteos y el ganador (en caso de empate, el primero que alcance el máximo de votos).
# difficulty: Intermedio
# expected_output: ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana')
# hint: Puedes usar un diccionario para acumular frecuencias recorriendo la lista, o utilizar 'get()' para simplificar la asignación. Luego, busca la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    if not conteo:
        return {}, None
    
    ganador = max(conteo, key=conteo.get)
    return conteo, ganador

# === TESTS ===
try:
    assert contar_votos(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana'), "Error: el test 1 ha fallado."
    assert contar_votos(["Luis", "Luis", "Maria", "Maria"]) == ({'Luis': 2, 'Maria': 2}, 'Luis'), "Error: considera casos límites en tu lógica."
    assert contar_votos([]) == ({}, None), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")