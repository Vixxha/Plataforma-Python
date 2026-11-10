# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que procese una lista de diccionarios que representan productos. La función debe filtrar aquellos productos cuyo precio sea menor o igual a un presupuesto máximo, ordenarlos de forma descendente según su precio (y ascendente por nombre en caso de empate), y finalmente buscar y devolver una lista con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado', 'Mouse']
# hint: Puedes usar list comprehensions para filtrar, sorted() con una clave múltiple para ordenar, y otra comprensión o un bucle para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar por presupuesto
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    
    # Ordenar: primero por precio descendente (-x['precio']), luego por nombre ascendente (x['nombre'])
    ordenados = sorted(filtrados, key=lambda x: (-x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Laptop", "precio": 800},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 50},
        {"nombre": "Monitor", "precio": 300}
    ]
    assert procesar_inventario(inv1, 500) == ['Monitor', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Zeta", "precio": 50},
        {"nombre": "Alfa", "precio": 50},
        {"nombre": "Beta", "precio": 10}
    ]
    assert procesar_inventario(inv2, 100) == ['Alfa', 'Zeta', 'Beta'], "Error: considera casos límites en tu lógica (empates en precio ordenados alfabéticamente)."
    
    assert procesar_inventario(inv1, 10) == [], "Error: el caso base falló (ningún producto cumple con el presupuesto)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")