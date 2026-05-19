# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a cero, los ordene de menor a mayor precio y finalmente retorne una lista con los nombres de los productos encontrados que coincidan con un precio máximo dado.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse']
# hint: Usa una lista de comprensión para filtrar, el método .sort() con una función lambda para ordenar y, finalmente, otra lista de comprensión para extraer los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, precio_maximo):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles if p['precio'] <= precio_maximo]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Laptop', 'precio': 500, 'stock': 2}
    ]
    assert filtrar_y_ordenar_productos(inventario, 600) == ['Mouse', 'Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 100) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")