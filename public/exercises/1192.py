# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios con productos (que contienen 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene por su precio de forma ascendente y finalmente busque y devuelva el nombre del producto más económico dentro de ese filtro. Si la lista filtrada está vacía, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Puedes usar listas por comprensión o la función filter para el filtrado, sorted para el ordenamiento y acceder al primer elemento si existe.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p.get('stock', 0) > 0]
    if not filtrados:
        return None
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Borrador", "precio": 1.5, "stock": 0}
    ]
    inv2 = [
        {"nombre": "Mochila", "precio": 45.0, "stock": 0},
        {"nombre": "Pluma", "precio": 5.0, "stock": 2}
    ]
    inv3 = [
        {"nombre": "Regla", "precio": 3.0, "stock": 0}
    ]
    
    assert procesar_inventario(inv1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == "Pluma", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")