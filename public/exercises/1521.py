# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por su nombre) y finalmente buscar y devolver una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el primer filtro, sorted con una clave múltiple (lambda) para el ordenamiento, y otra pasada para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_max):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(en_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Arroz', 'precio': 2.5, 'stock': 10},
        {'nombre': 'Leche', 'precio': 1.2, 'stock': 5},
        {'nombre': 'Pan', 'precio': 1.0, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 1.0, 'stock': 20},
        {'nombre': 'Carne', 'precio': 10.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 2.0) == ['Manzana', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 0.5) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 15.0) == ['Manzana', 'Leche', 'Arroz', 'Carne'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")