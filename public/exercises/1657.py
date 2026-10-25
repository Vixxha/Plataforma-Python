# === METADATA ===
# title: Gestión y Filtrado de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a 0, ordenarlos por su precio de forma ascendente (y en caso de tener el mismo precio, alfabéticamente por su nombre) y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor', 'Laptop']
# hint: Puedes usar las funciones filter() o una list comprehension para filtrar, y la función sorted() con una clave múltiple (lambda) para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Mouse', 'Teclado', 'Laptop'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Z', 'precio': 10, 'stock': 1},
        {'nombre': 'A', 'precio': 10, 'stock': 5}
    ]
    assert procesar_inventario(inv2) == ['A', 'Z'], "Error: considera casos límites en tu lógica (orden alfabético con igual precio)."
    
    inv3 = [
        {'nombre': 'Tablet', 'precio': 500, 'stock': 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló (ningún producto con stock)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")