# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos votados y devuelva un diccionario con la cantidad de votos obtenidos por cada uno, además de identificar al ganador. Debes retornar un diccionario que contenga el conteo de votos de todos los candidatos y una clave adicional llamada 'ganador' con el nombre del candidato más votado (en caso de empate, cualquiera de ellos).
# difficulty: Intermedio
# expected_output: {'Ana': 2, 'Carlos': 3, 'Beatriz': 1, 'ganador': 'Carlos'}
# hint: Utiliza un diccionario para ir acumulando las frecuencias de los votos iterando sobre la lista. Luego, puedes recorrer el diccionario para encontrar la clave con el valor máximo.

# === SOLUTION ===
def contar_votos(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = None
    max_votos = -1
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato
            
    conteo['ganador'] = ganador
    return conteo

# === TESTS ===
try:
    assert contar_votos(['Ana', 'Carlos', 'Ana', 'Carlos', 'Carlos', 'Beatriz']) == {'Ana': 2, 'Carlos': 3, 'Beatriz': 1, 'ganador': 'Carlos'}, "Error: el test 1 ha fallado."
    assert contar_votos(['Luis', 'Luis', 'Maria', 'Maria']) == {'Luis': 2, 'Maria': 2, 'ganador': 'Luis'}, "Error: considera casos límites en tu lógica."
    assert contar_votos(['Solo']) == {'Solo': 1, 'ganador': 'Solo'}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")