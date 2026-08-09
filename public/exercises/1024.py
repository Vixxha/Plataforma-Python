# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, buscar y devolver el nombre del producto más económico dentro de ese filtro. Si la lista filtrada está vacía, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Primero filtra usando una comprensión de lista, luego ordena la lista resultante utilizando sorted con una función lambda basada en el precio, y finalmente extrae el nombre del primer elemento si existe.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not disponibles:
        return None
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Retornar el nombre del producto más económico
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Cuaderno', 'precio': 15.5, 'stock': 10},
        {'nombre': 'Lápiz', 'precio': 2.0, 'stock': 25},
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 0}
    ]
    inv2 = [
        {'nombre': 'Tablet', 'precio': 200.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 15.0, 'stock': 5}
    ]
    inv3 = []

    assert procesar_inventario(inv1) == 'Lápiz', "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == 'Mouse', "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")