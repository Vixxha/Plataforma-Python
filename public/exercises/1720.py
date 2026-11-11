# === METADATA ===
# title: Gestión y Filtrado de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos cuyo stock sea mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con los nombres de los primeros N productos (donde N es un parámetro dado). Si hay productos con el mismo precio, mantén su orden relativo original.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone', 'Teclado']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted (o el método sort) con una función lambda como clave para el ordenamiento, y asegurarte de manejar correctamente el límite N.

# === SOLUTION ===
def procesar_inventario(productos, n):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma descendente (usando stable sort por defecto)
    ordenados = sorted(disponibles, key=lambda x: x['precio'], reverse=True)
    
    # Extraer los nombres de los primeros N productos
    resultado = [p['nombre'] for p in ordenados[:n]]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 3}
    ]
    
    assert procesar_inventario(inv1, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 5) == ['Laptop', 'Smartphone', 'Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")