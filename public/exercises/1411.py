# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente permita buscar y retornar el nombre del producto más barato que cumpla con una categoría o condición dada, o retornar una lista con los nombres de los productos filtrados y ordenados si no se especifica búsqueda. Para este ejercicio, la función debe filtrar el stock > 0, ordenar por precio ascendente y retornar la lista de nombres de dichos productos ordenados.
# difficulty: Intermedio
# expected_output: ["Laptop", "Mouse", "Teclado"]
# hint: Puedes usar list comprehensions o filter para el filtrado, y la función sorted() pasando una clave múltiple (lambda x: (x['precio'], x['nombre'])) para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    productos_ordenados = sorted(productos_disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer únicamente los nombres
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Teclado", "precio": 45.5, "stock": 10},
        {"nombre": "Mouse", "precio": 20.0, "stock": 0},
        {"nombre": "Laptop", "precio": 800.0, "stock": 3},
        {"nombre": "Monitor", "precio": 150.0, "stock": 5}
    ]
    assert procesar_inventario(inventario_1) == ["Teclado", "Monitor", "Laptop"], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {"nombre": "Z", "precio": 10.0, "stock": 2},
        {"nombre": "A", "precio": 10.0, "stock": 5},
        {"nombre": "B", "precio": 5.0, "stock": 0}
    ]
    assert procesar_inventario(inventario_2) == ["A", "Z"], "Error: considera casos límites en tu lógica (empates en precio)."
    
    inventario_3 = []
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")