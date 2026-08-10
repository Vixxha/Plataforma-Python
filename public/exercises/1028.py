# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente buscar y devolver una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una clave múltiple para el ordenamiento, y luego extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0 y precio <= presupuesto
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= presupuesto]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {'nombre': 'Mochila', 'precio': 50.0, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 15.0, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 2.0, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.0, 'stock': 20}
    ]
    assert procesar_inventario(inv, 20.0) == ['Lapicero', 'Cuaderno'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 60.0) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 1.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")