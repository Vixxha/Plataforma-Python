# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe retornar un diccionario con el recuento total de votos para cada candidato y, además, el nombre del candidato ganador. Si hay un empate en el primer lugar, se debe retornar cualquiera de ellos. La salida debe ser una tupla con el formato: (diccionario_recuento, nombre_ganador).
# difficulty: Intermedio
# expected_output: ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana')
# hint: Puedes usar un diccionario para contar las frecuencias iterando sobre la lista. Para encontrar el ganador, puedes recorrer las claves y valores del diccionario buscando el valor máximo.

# === SOLUTION ===
def contar_votos_y_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
        
    ganador = None
    max_votos = -1
    for candidato, total in conteo.items():
        if total > max_votos:
            max_votos = total
            ganador = candidato
            
    return conteo, ganador

# === TESTS ===
try:
    assert contar_votos_y_ganador(["Ana", "Carlos", "Ana", "Bea", "Carlos", "Ana"]) == ({'Ana': 3, 'Carlos': 2, 'Bea': 1}, 'Ana'), "Error: el test 1 ha fallado."
    assert contar_votos_y_ganador(["Luis", "Luis", "Maria"]) == ({'Luis': 2, 'Maria': 1}, 'Luis'), "Error: considera casos límites en tu lógica."
    assert contar_votos_y_ganador(["SoloUno"]) == ({'SoloUno': 1}, 'SoloUno'), "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")