# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente busque y devuelva una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una clave múltiple (tupla) para el ordenamiento, y una comprensión para extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    nombres = [p['nombre'] for p in ordenados]
    return nombres

# === TESTS ===
try:
    catalogo = [
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Cable HDMI", "precio": 10},
        {"nombre": "Audífonos", "precio": 45}
    ]
    
    assert filtrar_ordenar_productos(catalogo, 40) == ['Cable HDMI', 'Audífonos', 'Teclado', 'Monitor'] or filtrar_ordenar_productos(catalogo, 40) == ['Audífonos', 'Cable HDMI', 'Teclado', 'Monitor'] # Dependiendo de orden estable para iguales precios
    # Ajustemos un test más estricto con precios únicos o controlados:
    
    catalogo_2 = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Libreta", "precio": 5},
        {"nombre": "Mochila", "precio": 40},
        {"nombre": "Pluma", "precio": 2}
    ]
    assert filtrar_ordenar_productos(catalogo_2, 10) == ['Mochila', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(catalogo_2, 1000) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(catalogo_2, 0) == ['Pluma', 'Libreta', 'Mochila', 'Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")