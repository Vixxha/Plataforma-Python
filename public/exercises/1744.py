# === METADATA ===
# title: Gestión y Filtrado de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma descendente según su precio y, en caso de empate en el precio, alfabéticamente por su nombre. Finalmente, debe retornar una lista con los nombres de los productos ordenados.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado', 'Mouse']
# hint: Puedes usar la función `filter` o una comprensión de lista para eliminar los productos sin stock. Para el ordenamiento múltiple, utiliza el parámetro `key` de `sorted()` con una función lambda que devuelva una tupla.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio descendiente (-p['precio']) y por nombre ascendente (p['nombre'])
    ordenados = sorted(disponibles, key=lambda p: (-p['precio'], p['nombre']))
    
    # Extraer y retornar solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 3},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 200.0, 'stock': 5}
    ]
    assert procesar_inventario(inventario_1) == ['Laptop', 'Monitor', 'Mouse'], "Error: el test 1 ha fallado."

    inventario_2 = [
        {'nombre': 'Z', 'precio': 50.0, 'stock': 2},
        {'nombre': 'A', 'precio': 50