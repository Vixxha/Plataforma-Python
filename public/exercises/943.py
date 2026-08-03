# === METADATA ===
# title: Gestión y Filtrado de Inventario de Tienda
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente, y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para la condición, la función sorted con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    nombres_resultado = [p['nombre'] for p in productos_ordenados]
    return nombres_resultado

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Lapicero', 'precio': 1.20, 'stock': 100},
        {'nombre': 'Borrador', 'precio': 0.50, 'stock': 0},
        {'nombre': 'Cuaderno', 'precio': 3.50, 'stock': 12}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Teclado', 'precio': 25.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 15.0, 'stock': 3}
    ]
    assert procesar_inventario(inv2) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")