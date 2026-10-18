# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos cuyo stock sea mayor o igual a un valor mínimo, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una función lambda para el ordenamiento, y otra comprensión de lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p['stock'] >= stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    nombres = [p['nombre'] for p in ordenados]
    return nombres

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 2},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 8}
    ]
    
    assert procesar_inventario(inv1, 5) == ['Laptop', 'Smartphone', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 10) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv1, 20) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")