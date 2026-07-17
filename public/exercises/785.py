# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero usa un filtro (comprensión de listas o filter), luego ordena la lista resultante con sort o sorted, y finalmente extrae los nombres aplicando una condición extra.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio
    disponibles.sort(key=lambda x: x['precio'])
    # Filtrar por precio límite y extraer nombres
    return [p['nombre'] for p in disponibles if p['precio'] < limite_precio]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Impresora', 'precio': 150, 'stock': 0}
    ]
    assert procesar_inventario(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: debería devolver lista vacía si no hay productos bajo el precio."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}], 20) == ['A'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")