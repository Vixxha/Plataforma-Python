# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que tome una lista de diccionarios (con claves 'nombre' y 'precio'), filtre aquellos que cuestan menos de 10.0, ordene los resultados por nombre alfabéticamente y devuelva una lista con solo los nombres de dichas frutas.
# difficulty: Intermedio
# expected_output: ['Banana', 'Manzana']
# hint: Usa una lista de comprensión para el filtro, el método .sort() o sorted() para ordenar, y asegúrate de extraer solo los nombres al final.

# === SOLUTION ===
def filtrar_y_ordenar_frutas(inventario):
    filtrados = [fruta['nombre'] for fruta in inventario if fruta['precio'] < 10.0]
    filtrados.sort()
    return filtrados

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Manzana', 'precio': 5.5},
        {'nombre': 'Mango', 'precio': 12.0},
        {'nombre': 'Banana', 'precio': 3.2},
        {'nombre': 'Uva', 'precio': 15.0}
    ]
    assert filtrar_y_ordenar_frutas(inventario_ejemplo) == ['Banana', 'Manzana'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_frutas([{'nombre': 'Pera', 'precio': 20.0}]) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_frutas([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")