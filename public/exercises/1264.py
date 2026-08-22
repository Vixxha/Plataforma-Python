# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar la comprensión de listas o filter/map junto con sorted para ordenar los diccionarios basándote en la clave 'precio'.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, precio_limite):
    # Filtrar productos con stock > 0
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    
    # Filtrar por precio límite y extraer solo los nombres
    resultado = [p['nombre'] for p in productos_ordenados if p['precio'] <= precio_limite]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0},
        {"nombre": "USB", "precio": 15, "stock": 50}
    ]
    
    inventario_2 = [
        {"nombre": "Laptop", "precio": 1000, "stock": 2},
        {"nombre": "Audífonos", "precio": 50, "stock": 5}
    ]

    assert filtrar_y_ordenar_productos(inventario, 50) == ["USB", "Mouse"], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario_2, 30) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 250) == ["USB", "Mouse", "Monitor"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")