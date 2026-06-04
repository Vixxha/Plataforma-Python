# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que tome una lista de diccionarios (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor a 10.0, los ordene de forma ascendente por precio y finalmente busque el nombre del primer elemento resultante. Si no hay elementos, retorna None.
# difficulty: Intermedio
# expected_output: 'Manzana'
# hint: Usa una lista de comprensión para filtrar, el método sorted() con una función lambda para ordenar, y accede al índice [0] si la lista no está vacía.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] > 10.0]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return ordenados[0]['nombre'] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Pera', 'precio': 5.0},
        {'nombre': 'Manzana', 'precio': 15.0},
        {'nombre': 'Uva', 'precio': 20.0}
    ]
    assert procesar_inventario(inventario) == 'Manzana', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'Limón', 'precio': 5.0}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'A', 'precio': 50.0}, {'nombre': 'B', 'precio': 30.0}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")