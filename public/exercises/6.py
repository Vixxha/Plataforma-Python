# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que reciba una lista de diccionarios (con 'nombre' y 'precio'), filtre aquellos que cuestan menos de 2.0, los ordene alfabéticamente por nombre y retorne una lista con los nombres de las frutas resultantes.
# expected_output: ['fresa', 'limón', 'manzana']
# hint: Utiliza la función 'filter' o una lista por comprensión para filtrar, el método '.sort()' o la función 'sorted()' para ordenar, y una transformación para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(inventario):
    filtrados = [item['nombre'] for item in inventario if item['precio'] < 2.0]
    filtrados.sort()
    return filtrados

# === TESTS ===
try:
    data1 = [{'nombre': 'manzana', 'precio': 1.5}, {'nombre': 'mango', 'precio': 3.0}, {'nombre': 'limón', 'precio': 0.8}, {'nombre': 'fresa', 'precio': 1.2}]
    assert procesar_inventario(data1) == ['fresa', 'limón', 'manzana'], "Error: el test 1 ha fallado."
    
    data2 = [{'nombre': 'uva', 'precio': 5.0}, {'nombre': 'pera', 'precio': 4.0}]
    assert procesar_inventario(data2) == [], "Error: considera casos donde ningún elemento cumple la condición."
    
    data3 = [{'nombre': 'kiwi', 'precio': 1.9}]
    assert procesar_inventario(data3) == ['kiwi'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")