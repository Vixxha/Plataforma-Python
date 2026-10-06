# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves "nombre", "precio" y "stock"). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate en precio, alfabéticamente por su nombre), y finalmente retornar una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ["Manzana", "Pan", "Leche"]
# hint: Puedes usar listas por comprensión o la función filter para la condición, el método .sort() o la función sorted() con una clave múltiple (tupla) para el ordenamiento, y otra comprensión de lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p["stock"] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: (x["precio"], x["nombre"]))
    return [p["nombre"] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Manzana", "precio": 1.5, "stock": 10},
        {"nombre": "Leche", "precio": 1.2, "stock": 5},
        {"nombre": "Pan", "precio": 1.0, "stock": 0},
        {"nombre": "Arroz", "precio": 1.2, "stock": 20}
    ]
    assert procesar_inventario(inv1) == ["Leche", "Arroz", "Manzana"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Zeta", "precio": 10.0, "stock": 2},
        {"nombre": "Alfa", "precio": 5.0, "stock": 0},
        {"nombre": "Beta", "precio": 5.0, "stock": 3}
    ]
    assert procesar_inventario(inv2) == ["Beta", "Zeta"], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "C", "precio": 10, "stock": 0},
        {"nombre": "A", "precio": 5, "stock": 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")