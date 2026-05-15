# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra aquellos que cuestan menos de 100, ordénalos de menor a mayor precio y finalmente busca el nombre del producto más barato de la lista filtrada.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa un bucle o una list comprehension para el filtro, la función sorted() con una lambda para ordenar, y accede al primer elemento del resultado para encontrar el mínimo.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con precio menor a 100
    filtrados = [p for p in productos if p['precio'] < 100]
    
    # Ordenar por precio de menor a mayor
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Retornar el nombre del más barato o None si no hay elementos
    return ordenados[0]['nombre'] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200},
        {"nombre": "Teclado", "precio": 50},
        {"nombre": "Mouse", "precio": 30},
        {"nombre": "CPU", "precio": 500}
    ]
    assert procesar_inventario(inventario) == "Mouse", "Error: el test 1 ha fallado."
    assert procesar_inventario([{"nombre": "Caro", "precio": 500}]) == None, "Error: considera el caso donde no hay elementos bajo el umbral."
    assert procesar_inventario([{"nombre": "A", "precio": 10}, {"nombre": "B", "precio": 5}]) == "B", "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")