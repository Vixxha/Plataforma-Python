# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos cuyo stock sea mayor a 0, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los primeros N productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone', 'Teclado']
# hint: Puedes usar list comprehensions o filter para la condición, sorted con una función lambda para el ordenamiento, y slicing para limitar la cantidad de elementos.

# === SOLUTION ===
def procesar_inventario(productos, limite):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'], reverse=True)
    nombres_resultado = [p['nombre'] for p in productos_ordenados[:limite]]
    return nombres_resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 3},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 300.0, 'stock': 5},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_prueba, 3) == ['Laptop', 'Smartphone', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 1) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'Agotado', 'precio': 100.0, 'stock': 0}], 2) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")