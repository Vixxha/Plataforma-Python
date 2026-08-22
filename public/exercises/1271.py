# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente busque y retorne el nombre del producto más barato dentro de los filtrados. Si la lista filtrada está vacía, debe retornar una cadena vacía "".
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Puedes usar la función `filter` o una comprensión de lista para filtrar, el método `sort` o la función `sorted` con una clave múltiple para ordenar, y acceder al primer elemento si existe.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not disponibles:
        return ""
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    disponibles.sort(key=lambda x: (x['precio'], x['nombre']))
    
    # Retornar el nombre del producto más barato
    return disponibles[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 10},
        {"nombre": "Lápiz", "precio": 5.0, "stock": 25},
        {"nombre": "Mochila", "precio": 45.0, "stock": 0},
        {"nombre": "Borrador", "precio": 5.0, "stock": 5}
    ]
    inv2 = [
        {"nombre": "Laptop", "precio": 800.0, "stock": 0},
        {"nombre": "Mouse", "precio": 25.0, "stock": 2}
    ]
    inv3 = []

    assert procesar_inventario(inv1) == "Borrador", "Error: el test 1 ha fallado. Debe ordenar por precio y resolver empates alfabéticamente."
    assert procesar_inventario(inv2) == "Mouse", "Error: considera casos límites en tu lógica (ignorar stock 0)."
    assert procesar_inventario(inv3) == "", "Error: el caso base falló (inventario vacío)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")