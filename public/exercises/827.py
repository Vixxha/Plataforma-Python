# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para la condición, la función `sorted()` con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p["stock"] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x["precio"])
    return [p["nombre"] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Mochila", "precio": 45.5, "stock": 5},
        {"nombre": "Borrador", "precio": 0.5, "stock": 0},
        {"nombre": "Cuaderno", "precio": 3.0, "stock": 12},
        {"nombre": "Lapicero", "precio": 1.2, "stock": 25}
    ]
    assert procesar_inventario(inv1) == ["Lapicero", "Cuaderno", "Mochila"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Agotado", "precio": 10.0, "stock": 0},
        {"nombre": "Caro", "precio": 100.0, "stock": 2}
    ]
    assert procesar_inventario(inv2) == ["Caro"], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")