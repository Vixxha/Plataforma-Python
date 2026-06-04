# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra los productos que cuesten menos de 50, ordénalos de mayor a menor precio y devuelve una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado']
# hint: Usa una lista de comprensión o filter() para el filtrado, el método sort() o la función sorted() con una lambda para el ordenamiento, y una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 50]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Laptop', 'precio': 40}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Laptop', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'Caro', 'precio': 100}]) == [], "Error: debería filtrar todos los elementos."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}, {'nombre': 'B', 'precio': 5}]) == ['A', 'B'], "Error: el orden descendente falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")