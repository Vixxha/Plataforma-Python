# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma descendente según su precio y devuelva únicamente una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar list comprehensions o filter para eliminar los elementos sin stock, sorted con la función lambda para ordenar, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos):
    productos_con_stock = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 300.0, 'stock': 2}
    ]
    assert filtrar_y_ordenar_productos(inventario_1) == ['Laptop', 'Monitor', 'Mouse'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'A', 'precio': 10, 'stock': 0},
        {'nombre': 'B', 'precio': 20, 'stock': 0}
    ]
    assert filtrar_y_ordenar_productos(inventario_2) == [], "Error: considera casos límites en tu lógica."
    
    inventario_3 = [
        {'nombre': 'Zapatilla', 'precio': 50, 'stock': 4},
        {'nombre': 'Camisa', 'precio': 50, 'stock': 2}
    ]
    resultado = filtrar_y_ordenar_productos(inventario_3)
    assert len(resultado) == 2, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")