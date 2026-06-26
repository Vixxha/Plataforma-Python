# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que: 1) Filtre los productos que tengan un stock mayor a 5 unidades, 2) Ordene el resultado de menor a mayor según su precio, y 3) Busque y retorne solo el nombre del primer producto (el más barato) de la lista filtrada. Si no hay productos disponibles, retorna None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Puedes usar la función `filter` o una comprensión de listas, seguido del método `.sort()` o la función `sorted()`.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] > 5]
    if not filtrados:
        return None
    
    filtrados.sort(key=lambda x: x['precio'])
    return filtrados[0]['nombre']

# === TESTS ===
try:
    inventario_test = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 15, 'stock': 8},
        {'nombre': 'Webcam', 'precio': 50, 'stock': 12}
    ]
    assert procesar_inventario(inventario_test) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'Vacio', 'precio': 10, 'stock': 0}]) == None, "Error: debería retornar None si no hay stock."
    assert procesar_inventario([{'nombre': 'A', 'precio': 50, 'stock': 6}, {'nombre': 'B', 'precio': 30, 'stock': 6}]) == "B", "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")