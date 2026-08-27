# === METADATA ===
# title: Gestión y Búsqueda de Productos en el Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"), filtre aquellos productos cuyo stock sea mayor a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente busque y devuelva únicamente una lista con los nombres de los productos que cumplan con ambas condiciones.
# difficulty: Intermedio
# expected_output: ["Camisa", "Pantalón", "Zapatos"]
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una clave múltiple (lambda) para el ordenamiento, y una comprensión final para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p["stock"] > stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x["precio"], x["nombre"]))
    return [p["nombre"] for p in ordenados]

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Zapatos", "precio": 45.50, "stock": 10},
        {"nombre": "Gorra", "precio": 15.00, "stock": 2},
        {"nombre": "Camisa", "precio": 20.00, "stock": 15},
        {"nombre": "Pantalón", "precio": 35.00, "stock": 8},
        {"nombre": "Medias", "precio": 5.00, "stock": 0}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 5) == ["Gorra", "Camisa", "Pantalón", "Zapatos"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 20) == ["Zapatos"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 50) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")