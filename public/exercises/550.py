# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos con precio mayor a 50, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos resultantes. Si no hay productos, devuelve una lista vacía.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista filtrada usando el parámetro 'key' en la función sorted().

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] > 50]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 80}
    ]
    assert procesar_inventario(productos_test) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'Cable', 'precio': 10}]) == [], "Error: el filtro no excluyó correctamente."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")