# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente, y finalmente buscar y devolver el nombre del producto más económico dentro de ese filtro. Si no hay productos disponibles, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Primero filtra los elementos con stock > 0, luego ordénalos usando la función sorted() con una clave (key) basada en el precio, y finalmente extrae el nombre del primer elemento si la lista filtrada no está vacía.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    if not disponibles:
        return None
    disponibles_ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return disponibles_ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 10},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 50},
        {"nombre": "Mochila", "precio": 45.0, "stock": 0}
    ]
    inv2 = [
        {"nombre": "Laptop", "precio": 800.0, "stock": 0},
        {"nombre": "Mouse", "precio": 25.0, "stock": 2}
    ]
    inv3 = [
        {"nombre": "Borrador", "precio": 1.0, "stock": 0}
    ]
    
    assert procesar_inventario(inv1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == "Mouse", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")