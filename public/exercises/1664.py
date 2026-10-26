# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos que cumplan con una consulta de búsqueda (que coincida parcialmente y sin distinguir entre mayúsculas y minúsculas) dentro de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Tablet']
# hint: Puedes usar list comprehensions o filter para el filtro de stock, el método sorted() con una función lambda para ordenar por precio, y verificar si el término de búsqueda está en el nombre (convertido a minúsculas) para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, termino_busqueda):
    # Filtrar productos con stock mayor a 0
    con_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar de forma ascendente por precio
    ordenados = sorted(con_stock, key=lambda x: x['precio'])
    
    # Buscar productos que contengan el término (case-insensitive) y extraer sus nombres
    termino = termino_busqueda.lower()
    resultado = [p['nombre'] for p in ordenados if termino in p['nombre'].lower()]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.0, "stock": 5},
        {"nombre": "Teclado", "precio": 45.0, "stock": 0},
        {"nombre": "Monitor", "precio": 200.0, "stock": 3},
        {"nombre": "Tablet", "precio": 300.0, "stock": 7}
    ]
    
    assert procesar_inventario(inv1, "op") == ["Laptop"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, "a") == ["Mouse", "Tablet", "Laptop"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv1, "z") == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")