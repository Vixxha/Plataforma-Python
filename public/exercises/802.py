# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtra aquellos que cuestan menos de 50, ordénalos alfabéticamente por nombre y devuelve solo la lista de sus nombres.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse']
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() para ordenar, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con precio menor a 50
    filtrados = [p for p in productos if p['precio'] < 50]
    # Ordenar por nombre
    filtrados.sort(key=lambda x: x['nombre'])
    # Retornar lista de nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Teclado', 'precio': 60},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Laptop', 'precio': 45},
        {'nombre': 'Monitor', 'precio': 120}
    ]
    assert procesar_inventario(productos_test) == ['Laptop', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}, {'nombre': 'B', 'precio': 100}]) == ['A'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([]) == [], "Error: el caso base (lista vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")