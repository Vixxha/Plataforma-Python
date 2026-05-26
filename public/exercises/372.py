# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que reciba una lista de diccionarios (con 'nombre' y 'precio'), filtre aquellos con precio menor a 5.0, los ordene alfabéticamente por nombre y devuelva una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pera']
# hint: Usa un ciclo for o una lista de comprensión para filtrar, el método .sort() o la función sorted() para ordenar, y una lista por comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con precio menor a 5.0
    filtrados = [p for p in productos if p['precio'] < 5.0]
    # Ordenar por nombre
    filtrados.sort(key=lambda x: x['nombre'])
    # Extraer nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Zanahoria', 'precio': 2.5},
        {'nombre': 'Manzana', 'precio': 1.5},
        {'nombre': 'Aguacate', 'precio': 6.0},
        {'nombre': 'Pera', 'precio': 3.0}
    ]
    assert procesar_inventario(inventario) == ['Manzana', 'Pera', 'Zanahoria'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: debería devolver lista vacía si nada cumple la condición."
    assert procesar_inventario([]) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")