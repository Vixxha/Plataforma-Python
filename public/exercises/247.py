# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que tome una lista de diccionarios (frutas con nombre y precio). La función debe filtrar las frutas que cuestan menos de 2.0, ordenarlas alfabéticamente por nombre y devolver una lista con los nombres de las frutas resultantes.
# difficulty: Intermedio
# expected_output: ['banana', 'manzana']
# hint: Usa una lista de comprensión para el filtro, el método .sort() o la función sorted() para ordenar, y finalmente extrae solo los nombres.

# === SOLUTION ===
def procesar_inventario(frutas):
    # Filtrar frutas con precio menor a 2.0
    filtradas = [f for f in frutas if f['precio'] < 2.0]
    # Ordenar por nombre
    filtradas.sort(key=lambda x: x['nombre'])
    # Retornar solo los nombres
    return [f['nombre'] for f in filtradas]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'manzana', 'precio': 1.5},
        {'nombre': 'mango', 'precio': 3.0},
        {'nombre': 'banana', 'precio': 0.8},
        {'nombre': 'uva', 'precio': 2.5}
    ]
    assert procesar_inventario(inventario) == ['banana', 'manzana'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'a', 'precio': 5}]) == [], "Error: el filtro no eliminó correctamente."
    assert procesar_inventario([{'nombre': 'b', 'precio': 1.0}, {'nombre': 'a', 'precio': 0.5}]) == ['a', 'b'], "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")