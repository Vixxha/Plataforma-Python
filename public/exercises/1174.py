# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos ordenados cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno']
# hint: Puedes usar list comprehensions o filter para la condición inicial, la función sorted con una función lambda para ordenar por precio, y luego aplicar la búsqueda según el presupuesto.

# === SOLUTION ===
def filtrar_y_buscar_productos(inventario, presupuesto):
    # Filtrar productos con stock > 0
    disponibles = [p for p in inventario if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inv_prueba = [
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 5},
        {'nombre': 'Lapicero', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 0.5, 'stock': 0},
        {'nombre': 'Cuaderno', 'precio': 3.0, 'stock': 12}
    ]
    
    assert filtrar_y_buscar_productos(inv_prueba, 5.0) == ['Lapicero', 'Cuaderno'], "Error: el test 1 ha fallado."
    assert filtrar_y_buscar_productos(inv_prueba, 0.4) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_buscar_productos(inv_prueba, 50.0) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")