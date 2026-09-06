# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock mayor a cero, los ordene por precio de forma ascendente y permita buscar y retornar el nombre del producto más barato dentro de los filtrados. Si la lista filtrada está vacía, debe retornar None.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Puedes usar list comprehensions o filter para la condición del stock, la función sorted() con una función lambda para ordenar, y acceder al primer elemento del resultado.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not disponibles:
        return None
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Retornar el nombre del producto más barato
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Monitor", "precio": 150.0, "stock": 5},
        {"nombre": "Teclado", "precio": 25.5, "stock": 10},
        {"nombre": "Mouse", "precio": 15.0, "stock": 0}
    ]
    inv2 = [
        {"nombre": "Laptop", "precio": 1000.0, "stock": 0},
        {"nombre": "Cable HDMI", "precio": 10.0, "stock": 2}
    ]
    inv3 = [
        {"nombre": "Impresora", "precio": 200.0, "stock": 0}
    ]

    assert procesar_inventario(inv1) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == "Cable HDMI", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")