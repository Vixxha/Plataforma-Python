# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos que cuestan menos de 500, ordénalos de mayor a menor precio y busca el nombre del producto más caro resultante.
# difficulty: Intermedio
# expected_output: 'Laptop'
# hint: Usa un filtro (o comprensión de listas) para obtener los elementos menores a 500, la función sorted() con el argumento key=lambda, y finalmente accede al índice adecuado.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 500]
    if not filtrados:
        return None
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return ordenados[0]['nombre']

# === TESTS ===
try:
    data1 = [{'nombre': 'Mouse', 'precio': 20}, {'nombre': 'Teclado', 'precio': 150}, {'nombre': 'Laptop', 'precio': 450}]
    data2 = [{'nombre': 'Monitor', 'precio': 600}, {'nombre': 'Cable', 'precio': 10}]
    assert procesar_inventario(data1) == 'Laptop', "Error: el test 1 ha fallado."
    assert procesar_inventario(data2) == 'Cable', "Error: considera casos límites en tu lógica."
    assert procesar_inventario([]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")