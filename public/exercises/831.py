# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos que coincidan o contengan una cadena de búsqueda (ignorando mayúsculas/minúsculas).
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una función lambda para el ordenamiento por precio, y verificar subcadenas con el operador 'in' y .lower().

# === SOLUTION ===
def buscar_y_ordenar_productos(productos, termino_busqueda):
    # Filtrar productos con stock > 0
    productos_con_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x['precio'])
    
    # Filtrar por término de búsqueda (insensible a mayúsculas) y extraer solo los nombres
    termino = termino_busqueda.lower()
    resultado = [
        p['nombre'] for p in productos_ordenados 
        if termino in p['nombre'].lower()
    ]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 3},
        {'nombre': 'Mini Teclado', 'precio': 30.0, 'stock': 8}
    ]
    
    assert buscar_y_ordenar_productos(inventario, "teclado") == ['Mini Teclado'], "Error: el test 1 ha fallado."
    assert buscar_y_ordenar_productos(inventario, "o") == ['Mouse', 'Monitor', 'Laptop'], "Error: considera casos límites en tu lógica."
    assert buscar_y_ordenar_productos(inventario, "tablet") == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")