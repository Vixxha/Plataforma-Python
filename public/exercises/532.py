# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio), filtra aquellos que cuesten menos de 500, ordénalos de mayor a menor precio y devuelve los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Tablet', 'Monitor']
# hint: Usa un filtro (o comprensión de listas) para obtener los elementos menores a 500, luego utiliza el método sorted() con un parámetro key para ordenar de forma descendente.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos):
    filtrados = [p for p in productos if p['precio'] < 500]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    data = [
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Monitor', 'precio': 300},
        {'nombre': 'Mouse', 'precio': 50},
        {'nombre': 'Tablet', 'precio': 450}
    ]
    assert filtrar_y_ordenar_productos(data) == ['Tablet', 'Monitor', 'Mouse'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos([{'nombre': 'Caro', 'precio': 1000}]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")