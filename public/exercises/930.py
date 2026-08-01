# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios (productos, donde cada uno tiene 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio y finalmente busque y devuelva el nombre del producto más económico entre los filtrados. Si no hay productos disponibles, debe retornar una cadena indicando "Sin stock".
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Primero filtra los elementos con stock > 0, luego ordénalos usando la clave 'precio' (puedes usar sorted con una función lambda) y finalmente accede al nombre del primer elemento si la lista no está vacía.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    if not disponibles:
        return "Sin stock"
    
    disponibles_ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return disponibles_ordenados[0]['nombre']

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Mochila", "precio": 45.0, "stock": 2}
    ]
    inv2 = [
        {"nombre": "Borrador", "precio": 1.5, "stock": 0},
        {"nombre": "Regla", "precio": 3.0, "stock": 0}
    ]
    inv3 = [
        {"nombre": "Tablet", "precio": 200.0, "stock": 1},
        {"nombre": "Mouse", "precio": 25.0, "stock": 5},
        {"nombre": "Teclado", "precio": 45.0, "stock": 3}
    ]
    
    assert procesar_inventario(inv1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == "Sin stock", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) == "Mouse", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")