# === METADATA ===
# title: Gestión de Inventario Tech
# description: Crea una función que tome una lista de diccionarios (productos), filtre aquellos con precio mayor a 500, los ordene de forma ascendente según su precio y devuelva solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con sort o sorted, y finalmente extrae los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_inventario(productos):
    # Filtrar productos con precio > 500
    filtrados = [p for p in productos if p['precio'] > 500]
    # Ordenar por precio de forma ascendente
    filtrados.sort(key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Teclado', 'precio': 100},
        {'nombre': 'Monitor', 'precio': 800}
    ]
    assert filtrar_y_ordenar_inventario(inventario) == ['Monitor', 'Laptop'], "Error: el orden o filtrado es incorrecto."
    assert filtrar_y_ordenar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: no filtró correctamente productos baratos."
    assert filtrar_y_ordenar_inventario([{'nombre': 'B', 'precio': 600}, {'nombre': 'A', 'precio': 900}]) == ['B', 'A'], "Error: el orden ascendente falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")