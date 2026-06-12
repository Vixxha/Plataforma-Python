# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (nombre y precio), crea una función que filtre los productos que cuestan menos de 50, los ordene de menor a mayor precio y retorne una lista con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Leche', 'Pan']
# hint: Primero utiliza una lista de comprensión para filtrar, luego el método .sort() o la función sorted() usando una función lambda como llave de ordenamiento.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos):
    filtrados = [p for p in productos if p['precio'] < 50]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Pan', 'precio': 15},
        {'nombre': 'Leche', 'precio': 30},
        {'nombre': 'Monitor', 'precio': 150}
    ]
    assert filtrar_y_ordenar_productos(inventario) == ['Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos([{'nombre': 'Caramelo', 'precio': 5}]) == ['Caramelo'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos([{'nombre': 'TV', 'precio': 200}]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")