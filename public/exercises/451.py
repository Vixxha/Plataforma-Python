# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Dada una lista de diccionarios con nombres y precios de frutas, filtra aquellas que cuestan menos de 2.0, ordénalas alfabéticamente por nombre y busca si una fruta específica existe en la lista filtrada.
# difficulty: Intermedio
# expected_output: True o False tras procesar la lista
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() para ordenar, y el operador 'in' o un bucle para la búsqueda.

# === SOLUTION ===
def gestionar_inventario(inventario, limite_precio, fruta_objetivo):
    # Filtrar frutas por precio
    filtradas = [f['nombre'] for f in inventario if f['precio'] < limite_precio]
    # Ordenar alfabéticamente
    filtradas.sort()
    # Buscar si la fruta está en la lista resultante
    return fruta_objetivo in filtradas

# === TESTS ===
try:
    inventario = [
        {'nombre': 'manzana', 'precio': 1.5},
        {'nombre': 'banana', 'precio': 2.5},
        {'nombre': 'cereza', 'precio': 1.2},
        {'nombre': 'durazno', 'precio': 3.0}
    ]
    assert gestionar_inventario(inventario, 2.0, 'manzana') == True, "Error: el test 1 ha fallado."
    assert gestionar_inventario(inventario, 2.0, 'banana') == False, "Error: considera casos límites en tu lógica."
    assert gestionar_inventario(inventario, 5.0, 'durazno') == True, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")