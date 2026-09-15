# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"), filtre aquellos productos cuyo stock sea mayor a un valor mínimo dado, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente busque y devuelva una lista solo con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una clave múltiple (lambda) para el ordenamiento, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p["stock"] > stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x["precio"], x["nombre"]))
    return [p["nombre"] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 10},
        {"nombre": "Borrador", "precio": 2.0, "stock": 3},
        {"nombre": "Lapicero", "precio": 5.0, "stock": 25},
        {"nombre": "Mochila", "precio": 45.0, "stock": 5}
    ]
    assert procesar_inventario(inv1, 4) == ["Borrador", "Lapicero", "Cuaderno", "Mochila"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Tablet", "precio": 300, "stock": 2},
        {"nombre": "Laptop", "precio": 300, "stock": 10},
        {"nombre": "Mouse", "precio": 25, "stock": 15}
    ]
    assert procesar_inventario(inv2, 5) == ["Mouse", "Laptop"], "Error: considera casos límites en tu lógica (empates de precio deben ordenarse alfabéticamente por nombre)."
    
    assert procesar_inventario(inv1, 50) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")