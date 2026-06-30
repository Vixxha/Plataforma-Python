# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtra los productos que cuesten menos de 50, ordénalos de forma ascendente por precio y devuelve únicamente una lista con los nombres de esos productos.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar una lista de comprensión o filter() para el filtrado, y la función sorted() con un argumento 'key' para el ordenamiento.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos):
    # Filtrar productos con precio menor a 50
    filtrados = [p for p in productos if p['precio'] < 50]
    # Ordenar por precio de menor a mayor
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Monitor', 'precio': 200},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Laptop', 'precio': 800}
    ]
    assert filtrar_y_ordenar_productos(productos_test) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos([{'nombre': 'A', 'precio': 10}]) == ['A'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos([{'nombre': 'B', 'precio': 100}]) == [], "Error: el caso base (sin coincidencias) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")