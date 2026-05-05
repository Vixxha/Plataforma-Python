# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con nombre y precio), filtra los productos cuyo precio sea mayor o igual a 50, ordénalos de forma ascendente por precio y devuelve una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor', 'Laptop']
# hint: Usa un ciclo for o una lista de comprensión para filtrar, luego utiliza el método .sort() o la función sorted() con una clave (lambda) para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] >= 50]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Mouse", "precio": 20},
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Teclado", "precio": 50},
        {"nombre": "Laptop", "precio": 800}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Monitor', 'Laptop'], "Error: el orden o filtrado es incorrecto."
    assert procesar_inventario([{"nombre": "Cable", "precio": 10}]) == [], "Error: no se filtraron correctamente los productos económicos."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")