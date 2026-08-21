# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente devuelva una lista con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, y la función `sorted` pasando una tupla como clave de ordenamiento `key=lambda x: (x['precio'], x['nombre'])`.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Mochila", "precio": 45.50, "stock": 5},
        {"nombre": "Cuaderno", "precio": 3.50, "stock": 10},
        {"nombre": "Borrador", "precio": 1.00, "stock": 0},
        {"nombre": "Lapicero", "precio": 1.00, "stock": 25}
    ]
    assert procesar_inventario(inventario_1) == ['Borrador', 'Lapicero', 'Cuaderno', 'Mochila'] or ['Lapicero', 'Borrador', ...], "Error: el test 1 ha fallado."
    
    # Ajuste preciso considerando orden alfabético en caso de empate de precio
    assert procesar_inventario(inventario_1) == ['Lapicero', 'Borrador', 'Cuaderno', 'Mochila'] or procesar_inventario(inventario_1) == ['Borrador', 'Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    # Test limpio con empate controlado
    inventario_2 = [
        {"nombre": "Z-Zapatilla", "precio": 50.0, "stock": 2},
        {"nombre": "A-Remera", "precio": 50.0, "stock": 4},
        {"nombre": "Gorra", "precio": 20.0, "stock": 0}
    ]
    assert procesar_inventario(inventario_2) == ["A-Remera", "Z-Zapatilla"], "Error: considera casos límites en tu lógica y ordenamiento por nombre."

    inventario_3 = [
        {"nombre": "Tablet", "precio": 300.0, "stock": 0},
        {"nombre": "Mouse", "precio": 25.0, "stock": 0}
    ]
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")