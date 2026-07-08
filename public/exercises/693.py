# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra los productos que cuestan 50 o más, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos resultantes. Si hay productos con el mismo precio, mantén el orden alfabético por nombre.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor', 'Servidor']
# hint: Puedes usar el método .sort() o la función sorted() con una llave (key) que maneje múltiples criterios mediante una tupla (precio, nombre).

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] >= 50]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    data1 = [{'nombre': 'Mouse', 'precio': 20}, {'nombre': 'Monitor', 'precio': 150}, {'nombre': 'Laptop', 'precio': 500}, {'nombre': 'Teclado', 'precio': 45}, {'nombre': 'Servidor', 'precio': 800}]
    assert procesar_inventario(data1) == ['Monitor', 'Laptop', 'Servidor'], "Error: el test 1 ha fallado."
    
    data2 = [{'nombre': 'A', 'precio': 100}, {'nombre': 'B', 'precio': 100}, {'nombre': 'C', 'precio': 10}]
    assert procesar_inventario(data2) == ['A', 'B'], "Error: considera casos límites en tu lógica."
    
    assert procesar_inventario([]) == [], "Error: el caso base (lista vacía) falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")