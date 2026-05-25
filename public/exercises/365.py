# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos cuyo precio sea mayor a 50, ordénalos de forma ascendente por precio y devuelve solo los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con sort o sorted, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con precio mayor a 50
    filtrados = [p for p in productos if p['precio'] > 50]
    # Ordenar por precio ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Extraer nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 80}
    ]
    assert procesar_inventario(productos_test) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: considera casos donde no hay elementos que cumplan el filtro."
    assert procesar_inventario([{'nombre': 'X', 'precio': 100}, {'nombre': 'Y', 'precio': 60}]) == ['Y', 'X'], "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")