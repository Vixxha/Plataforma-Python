# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'), filtre aquellos cuyo stock sea mayor a un valor mínimo, busque y devuelva una lista con los nombres de los productos que cumplan con la condición, ordenados de forma descendente según su precio.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes utilizar una comprensión de lista o filter/map junto con la función sorted y su parámetro 'key' para ordenar de manera descendente.

# === SOLUTION ===
def filtrar_y_ordenar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p['stock'] > stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 2},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 8}
    ]
    
    assert filtrar_y_ordenar_inventario(inv1, 4) == ['Laptop', 'Smartphone', 'Mouse'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_inventario(inv1, 9) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_inventario(inv1, 20) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")