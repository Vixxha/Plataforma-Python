# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a 0, los ordene por precio de forma ascendente, y finalmente busque y devuelva el nombre del producto más económico dentro de los filtrados. Si no hay productos disponibles, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Puedes usar las funciones integradas de Python para filtrar y ordenar listas de diccionarios utilizando una función lambda como clave (key).

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not productos_disponibles:
        return None
        
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    
    return productos_ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Cuaderno", "precio": 15.50, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.00, "stock": 10},
        {"nombre": "Mochila", "precio": 45.00, "stock": 0}
    ]
    inventario_2 = [
        {"nombre": "Borrador", "precio": 1.50, "stock": 0},
        {"nombre": "Regla", "precio": 3.00, "stock": 0}
    ]
    inventario_3 = [
        {"nombre": "Tablet", "precio": 200.0, "stock": 2},
        {"nombre": "Mouse", "precio": 25.0, "stock": 15}
    ]
    
    assert procesar_inventario(inventario_1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_2) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_3) == "Mouse", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")