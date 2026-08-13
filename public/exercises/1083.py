# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente, y finalmente buscar y devolver el nombre del producto más económico dentro de ese filtro. Si no hay productos disponibles, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Primero filtra los elementos usando una comprensión de lista o filter(), luego ordénalos usando sorted() con una función lambda, y finalmente extrae el nombre del primer elemento si la lista no está vacía.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    if not disponibles:
        return None
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Borrador", "precio": 1.5, "stock": 0}
    ]
    inv2 = [
        {"nombre": "Mochila", "precio": 45.0, "stock": 0},
        {"nombre": "Regla", "precio": 5.0, "stock": 2}
    ]
    inv3 = [
        {"nombre": "Laptop", "precio": 800.0, "stock": 0}
    ]
    
    assert procesar_inventario(inv1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == "Regla", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")