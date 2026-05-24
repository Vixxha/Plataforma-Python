# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra los productos que cuesten más de 50, ordénalos de menor a mayor precio y devuelve solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa una lista de comprensión o filter() para el filtro, el método .sort() o sorted() para ordenar, y finalmente recorre la lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] > 50]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 80}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: considera casos límites donde ningún producto cumple el filtro."
    assert procesar_inventario([{'nombre': 'B', 'precio': 100}, {'nombre': 'C', 'precio': 200}]) == ['B', 'C'], "Error: el orden no es ascendente."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")