# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente por su precio y finalmente busque y devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Audífonos']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una función `lambda` para ordenar por precio, y otra pasada para extraer los nombres según el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_y_buscar(productos, presupuesto_max):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    
    # Buscar y extraer nombres de productos dentro del presupuesto
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2},
        {'nombre': 'Audífonos', 'precio': 50, 'stock': 8}
    ]
    
    assert filtrar_ordenar_y_buscar(inventario, 60) == ['Mouse', 'Audífonos'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_y_buscar(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_y_buscar([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")