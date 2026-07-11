# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que: 1) Filtre los productos que tengan un stock mayor a 5, 2) Ordene los resultados de forma ascendente según su precio, y 3) Busque y retorne solo el nombre del producto más barato dentro de ese filtro. Si no hay productos, retorna None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Primero usa una lista por comprensión para filtrar, luego el método .sort() o la función sorted() con una llave lambda, y finalmente accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] > 5]
    if not filtrados:
        return None
    
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 25, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 8},
        {'nombre': 'Webcam', 'precio': 60, 'stock': 12}
    ]
    assert procesar_inventario(inventario) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 2}]) == None, "Error: el caso de stock insuficiente falló."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50, 'stock': 10}, {'nombre': 'C', 'precio': 20, 'stock': 20}]) == "C", "Error: la lógica de ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")