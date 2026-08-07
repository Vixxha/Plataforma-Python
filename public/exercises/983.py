# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves "nombre", "precio" y "stock"). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para el ordenamiento por precio, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_con_stock = [p for p in productos if p["stock"] > 0]
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x["precio"])
    return [p["nombre"] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Monitor", "precio": 200.0, "stock": 5},
        {"nombre": "Mouse", "precio": 25.0, "stock": 10},
        {"nombre": "Teclado", "precio": 50.0, "stock": 0},
        {"nombre": "Audífonos", "precio": 45.0, "stock": 2}
    ]
    assert procesar_inventario(inv1) == ["Audífonos", "Mouse", "Monitor"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Laptop", "precio": 1000.0, "stock": 0},
        {"nombre": "USB", "precio": 10.0, "stock": 50}
    ]
    assert procesar_inventario(inv2) == ["USB"], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")