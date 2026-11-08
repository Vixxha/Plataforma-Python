# === METADATA ===
# title: Conteo de Votos y Ganador
# description: Escribe una función que reciba una lista de nombres de candidatos que han recibido votos. La función debe procesar esta lista y retornar un diccionario donde las claves sean los nombres de los candidatos y los valores sean el número total de votos que obtuvo cada uno. Finalmente, debe identificar y retornar el nombre del candidato con más votos (en caso de empate, el primero que aparezca en el diccionario).
# difficulty: Intermedio
# expected_output: {'Ana': 3, 'Carlos': 2, 'Beatriz': 1}
# hint: Puedes utilizar un diccionario para llevar la frecuencia de cada candidato iterando sobre la lista, y luego usar la función max() con una clave personalizada para encontrar al ganador.

# === SOLUTION ===
def contar_y_ganador(votos):
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    
    ganador = max(conteo, key=conteo.get)
    return {"conteo": conteo, "ganador": ganador}

# === TESTS ===
try:
    resultado_1 = contar_y_ganador(["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"])
    assert resultado_1 == {"conteo": {"Ana": 3, "Carlos": 2, "Beatriz": 1}, "ganador": "Ana"}, "Error: el test 1 ha fallado."
    
    resultado_2 = contar_y_ganador(["Pedro", "Pedro", "Juan", "Juan"])
    assert resultado_2 == {"conteo": {"Pedro": 2, "Juan": 2}, "ganador": "Pedro"}, "Error: considera casos límites en tu lógica."
    
    resultado_3 = contar_y_ganador(["Maria"])
    assert resultado_3 == {"conteo": {"Maria": 1}, "ganador": "Maria"}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")