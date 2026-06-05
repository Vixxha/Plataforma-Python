# === METADATA ===
# title: Gestión de Inventario Filtrado y Ordenado
# description: Dado una lista de diccionarios que representan productos (nombre y precio), desarrolla una función que filtre aquellos con un precio superior a un umbral dado y devuelva una lista con los nombres de estos productos ordenados alfabéticamente.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Utiliza una lista de comprensión para el filtrado y el método .sort() o la función sorted() para el ordenamiento.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, umbral):
    filtrados = [p['nombre'] for p in productos if p['precio'] > umbral]
    filtrados.sort()
    return filtrados

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Monitor', 'precio': 150}
    ]
    assert filtrar_y_ordenar_productos(inventario, 50) == ['Laptop', 'Monitor'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 500) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 1000) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")