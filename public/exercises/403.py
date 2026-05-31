# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los resultados restantes de forma descendente por precio y devuelve solo los nombres de los productos cuyo precio es mayor a 50.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Usa una lista de comprensión o filtros para eliminar el stock bajo, luego usa el método sort() o la función sorted() con una llave lambda.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor o igual a 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar descendentemente por precio
    filtrados.sort(key=lambda x: x['precio'], reverse=True)
    
    # Seleccionar nombres con precio > 50
    resultado = [p['nombre'] for p in filtrados if p['precio'] > 50]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 6}
    ]
    assert procesar_inventario(inventario) == ['Laptop', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: no debe incluir productos baratos."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")