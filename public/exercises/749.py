# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos que cuestan menos de 500, ordénalos por precio de forma ascendente y busca el nombre del producto más barato resultante. Si la lista filtrada está vacía, devuelve None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Primero usa una lista por comprensión para filtrar, luego el método sort() o la función sorted() para ordenar, y finalmente accede al primer elemento.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 500]
    if not filtrados:
        return None
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Monitor", "precio": 300}
    ]
    assert procesar_inventario(inventario) == "Mouse", "Error: el test 1 ha fallado."
    assert procesar_inventario([{"nombre": "GPU", "precio": 800}]) == None, "Error: considera casos donde no hay productos baratos."
    assert procesar_inventario([{"nombre": "Cable", "precio": 10}, {"nombre": "USB", "precio": 5}]) == "USB", "Error: el ordenamiento no es correcto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")