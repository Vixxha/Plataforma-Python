# === METADATA ===
# title: Gestión de Inventario con Filtros
# description: Crea una función que reciba una lista de diccionarios (productos), filtre aquellos con stock mayor a cero, los ordene alfabéticamente por nombre y busque si un producto específico existe en la lista resultante.
# difficulty: Intermedio
# expected_output: ['Arroz', 'Frijoles', 'Leche'] y True (si existe)
# hint: Usa un filtro (o list comprehension), el método .sort() o sorted() con una llave lambda, y el operador 'in' para la búsqueda.

# === SOLUTION ===
def gestionar_inventario(productos, nombre_busqueda):
    # Filtrar productos con stock > 0
    filtrados = [p['nombre'] for p in productos if p['stock'] > 0]
    # Ordenar alfabéticamente
    filtrados.sort()
    # Buscar si el nombre existe
    existe = nombre_busqueda in filtrados
    return filtrados, existe

# === TESTS ===
try:
    data = [
        {'nombre': 'Leche', 'stock': 5},
        {'nombre': 'Pan', 'stock': 0},
        {'nombre': 'Arroz', 'stock': 10},
        {'nombre': 'Frijoles', 'stock': 2}
    ]
    resultado_lista, resultado_busqueda = gestionar_inventario(data, 'Arroz')
    assert resultado_lista == ['Arroz', 'Frijoles', 'Leche'], "Error: El filtrado u ordenamiento es incorrecto."
    assert resultado_busqueda == True, "Error: La búsqueda no encontró el elemento existente."
    assert gestionar_inventario(data, 'Pan')[1] == False, "Error: Se incluyó un producto con stock 0."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")