# === METADATA ===
# title: Gestión y Filtrado de Inventario de Videojuegos
# description: Escribe una función que reciba una lista de diccionarios que representan videojuegos (con claves 'nombre', 'precio' y 'rating'). La función debe filtrar los juegos que tengan un rating mayor o igual a 4.0, ordenarlos por precio de forma ascendente (y en caso de empate, por nombre alfabéticamente), y finalmente retornar una lista únicamente con los nombres de los juegos que cumplan con la condición.
# difficulty: Intermedio
# expected_output: ['Celeste', 'Hades', 'Elden Ring']
# hint: Puedes usar la función `filter` o una comprensión de lista para filtrar, y la función `sorted` con una clave personalizada (lambda) para ordenar por múltiples criterios (precio y luego nombre).

# === SOLUTION ===
def filtrar_y_ordenar_juegos(juegos):
    # Filtrar juegos con rating >= 4.0
    juegos_filtrados = [j for j in juegos if j.get('rating', 0) >= 4.0]
    
    # Ordenar primero por precio ascendente, luego por nombre alfabéticamente
    juegos_ordenados = sorted(juegos_filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [juego['nombre'] for juego in juegos_ordenados]

# === TESTS ===
try:
    juegos_prueba = [
        {"nombre": "Elden Ring", "precio": 40.0, "rating": 4.8},
        {"nombre": "Cyberpunk 2077", "precio": 40.0, "rating": 3.2},
        {"nombre": "Hades", "precio": 25.0, "rating": 4.9},
        {"nombre": "Celeste", "precio": 20.0, "rating": 4.5},
        {"nombre": "Juego Malo", "precio": 10.0, "rating": 2.0}
    ]
    
    assert filtrar_y_ordenar_juegos(juegos_prueba) == ['Celeste', 'Hades', 'Elden Ring'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_juegos([]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_juegos([{"nombre": "Solo", "precio": 60.0, "rating": 3.9}]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")