# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre y precio), filtra aquellos que cuestan menos de 500, ordénalos de mayor a menor precio y busca el nombre del producto más caro resultante. Si no hay productos, retorna None.
# difficulty: Intermedio
# expected_output: 'Laptop'
# hint: Usa un filtro para los precios, luego el método sort o la función sorted con un parámetro key, y finalmente accede al primer elemento de la lista ordenada.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 500]
    if not filtrados:
        return None
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Monitor', 'precio': 300},
        {'nombre': 'Laptop', 'precio': 1200}
    ]
    assert procesar_inventario(inventario) == 'Monitor', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'Cargador', 'precio': 800}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")