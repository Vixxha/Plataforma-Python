# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra aquellos cuyo precio sea mayor o igual a 50, ordénalos de forma ascendente por precio y devuelve solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor', 'Servidor']
# hint: Puedes usar la función filter() o una lista por comprensión para filtrar, y luego el método .sort() o la función sorted() con una expresión lambda para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con precio >= 50
    filtrados = [p for p in productos if p['precio'] >= 50]
    # Ordenar por precio de forma ascendente
    filtrados.sort(key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    data = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Servidor', 'precio': 1200}
    ]
    assert procesar_inventario(data) == ['Monitor', 'Laptop', 'Servidor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: debería devolver lista vacía si nada cumple la condición."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50}, {'nombre': 'A', 'precio': 60}]) == ['B', 'A'], "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")