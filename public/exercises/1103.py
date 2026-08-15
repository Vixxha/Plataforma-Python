# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que procese una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor o igual a un valor mínimo dado, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una función lambda para el ordenamiento por precio, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p['stock'] >= stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.0, "stock": 5},
        {"nombre": "Teclado", "precio": 45.0, "stock": 2},
        {"nombre": "Monitor", "precio": 200.0, "stock": 0}
    ]
    
    assert procesar_inventario(inv, 2) == ['Laptop', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 10) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 20) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")