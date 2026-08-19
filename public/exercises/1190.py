# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente busque y devuelva únicamente el nombre del primer producto que coincida con una palabra clave de búsqueda en su nombre (insensible a mayúsculas), o None si ninguno coincide.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Puedes usar la función filter o list comprehensions para filtrar, sorted con una tupla como clave (key) para el ordenamiento múltiple, y un bucle o next() con una condición para la búsqueda.

# === SOLUTION ===
def procesar_productos(productos, precio_minimo, palabra_clave):
    # Filtrar por precio mínimo
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    
    # Ordenar por precio ascendente, y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Buscar el primer producto que contenga la palabra clave (insensible a mayúsculas)
    palabra_lower = palabra_clave.lower()
    for p in ordenados:
        if palabra_lower in p['nombre'].lower():
            return p['nombre']
            
    return None

# === TESTS ===
try:
    catalogo = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado Mecánico", "precio": 80},
        {"nombre": "Teclado Membrana", "precio": 25},
        {"nombre": "Monitor", "precio": 300}
    ]
    
    assert procesar_productos(catalogo, 50, "teclado") == "Teclado Membrana", "Error: el test 1 ha fallado."
    assert procesar_productos(catalogo, 500, "laptop") == "Laptop", "Error: considera casos límites en tu lógica."
    assert procesar_productos(catalogo, 1000, "mouse") is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")