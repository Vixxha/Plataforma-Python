# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre aquellos productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente devuelva solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Usa un filtro (o comprensión de listas) para el stock, el método .sort() o sorted() con una función lambda para el precio, y una lista de comprensión final para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 80, 'stock': 3}
    ]
    # Caso donde se filtra el stock=0 (Teclado) y se ordenan por precio: Mouse(20), Auriculares(80), Monitor(200)
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: El filtrado u ordenamiento no es correcto."
    
    inventario_vacio = [{'nombre': 'PC', 'precio': 1000, 'stock': 0}]
    assert procesar_inventario(inventario_vacio) == [], "Error: Debería retornar una lista vacía si no hay stock."
    
    inventario_ordenado = [{'nombre': 'A', 'precio': 10, 'stock': 1}, {'nombre': 'B', 'precio': 5, 'stock': 1}]
    assert procesar_inventario(inventario_ordenado) == ['B', 'A'], "Error: No se está ordenando correctamente por precio."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")