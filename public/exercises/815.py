# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra los productos que cuestan menos de 50, ordénalos de mayor a menor precio y devuelve una lista con los nombres resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado']
# hint: Usa un filtro (o comprensión de listas) para la condición de precio, luego el método sort() o la función sorted() con el parámetro 'reverse'.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 50]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    data1 = [{'nombre': 'Mouse', 'precio': 20}, {'nombre': 'Monitor', 'precio': 150}, {'nombre': 'Teclado', 'precio': 45}]
    assert procesar_inventario(data1) == ['Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    
    data2 = [{'nombre': 'A', 'precio': 10}, {'nombre': 'B', 'precio': 5}, {'nombre': 'C', 'precio': 40}]
    assert procesar_inventario(data2) == ['C', 'A', 'B'], "Error: considera casos límites en tu lógica."
    
    data3 = [{'nombre': 'Caro', 'precio': 500}]
    assert procesar_inventario(data3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")