# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra aquellos cuyo precio sea mayor o igual a 20, ordénalos de forma ascendente según su precio y devuelve una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor', 'Impresora']
# hint: Primero utiliza una lista de comprensión o filter para seleccionar los productos, luego emplea el método sort o la función sorted con una función lambda como clave de ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] >= 20]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    data1 = [{'nombre': 'Mouse', 'precio': 10}, {'nombre': 'Teclado', 'precio': 25}, {'nombre': 'Monitor', 'precio': 150}, {'nombre': 'Impresora', 'precio': 80}]
    assert procesar_inventario(data1) == ['Teclado', 'Impresora', 'Monitor'], "Error: el test 1 ha fallado."
    
    data2 = [{'nombre': 'USB', 'precio': 5}, {'nombre': 'Cable', 'precio': 10}]
    assert procesar_inventario(data2) == [], "Error: considera casos donde ningún elemento cumple el filtro."
    
    data3 = [{'nombre': 'A', 'precio': 100}, {'nombre': 'B', 'precio': 50}]
    assert procesar_inventario(data3) == ['B', 'A'], "Error: el ordenamiento ascendente falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")